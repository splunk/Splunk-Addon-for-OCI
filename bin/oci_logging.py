# The Universal Permissive License (UPL), Version 1.0
#
# Copyright (c) 2021, Oracle and/or its affiliates.  All rights reserved.
#
# Subject to the condition set forth below, permission is hereby granted to any person obtaining a copy of this software, associated documentation and/or data (collectively the "Software"), free of charge and under any and all copyright rights in the Software, and any and all patent rights owned or freely licensable by each licensor hereunder covering either (i) the unmodified Software as contributed to or provided by such licensor, or (ii) the Larger Works (as defined below), to deal in both
#
# (a) the Software, and
# (b) any piece of software and/or hardware listed in the lrgrwrks.txt file if one is included with the Software (each a "Larger Work" to which the Software is contributed by such licensors),
#
# without restriction, including without limitation the rights to copy, create derivative works of, display, perform, and distribute the Software and make, use, sell, offer for sale, import, export, have made, and have sold the Software and the Larger Work(s), and to sublicense the foregoing rights on either these or other terms.
#
# This license is subject to the following condition:
#
# The above copyright notice and either this complete permission notice or at a minimum a reference to the UPL must be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# encoding = utf-8
# module imports
import traceback
import os
import sys
import time
import signal
import json
import oci
import multiprocess as mp
import uuid
import logging as logger
# Imports for Splunk Libraries
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from base64 import b64encode, b64decode
from urllib.parse import urlparse
from splunklib import six
from connectivity_lib.stream import *
import splunklib.client as client
from splunklib.modularinput import *

# For debugging change ERROR to DEBUG
logger.basicConfig(level=logger.ERROR, format='%(asctime)s %(levelname)s %(message)s',
                   filename=os.path.join(os.environ['SPLUNK_HOME'], 'var', 'log', 'splunk', 'oci_logging.log'), filemode='a')

guid = str(uuid.uuid4())
global_stream_clients = {}
active = "true"
retries = 5
global_cursors = {}
global_retries = {}
global_interval = 90



def get_cursor_by_group(sc, sid, group_name, opt_part):
        global global_cursors
        try:
            cursor_details = oci.streaming.models.CreateGroupCursorDetails(group_name=group_name, instance_name=guid + opt_part, type=oci.streaming.models.CreateGroupCursorDetails.TYPE_LATEST, commit_on_get=True)
            response = sc.create_group_cursor(sid, cursor_details)
            logger.debug(str(response.data))
            logger.debug(str(response.headers))
            logger.debug(str(response.status))
            logger.debug(str(hasattr(response, 'data')))
            if hasattr(response, 'data'):
                global_cursors[str(opt_part)] = str(response.data.value)
                return str(response.data.value)
            else:
                time.sleep(int(global_interval))
                cursor = get_cursor_by_group(sc, sid, group_name, opt_part)
                return None

        except oci.exceptions.ServiceError as e:
            if e.status == 429:
                logger.debug("Error Fetching Cursor. Sleep and Retry: " + str(global_interval))
                time.sleep(int(global_interval))
                return ("Error Fetching Cursor. Sleep and Retry: " + str(global_interval))
            sys.exit()


def get_messages(config_items, cursor, i):
    logger.debug("function: entering get_messages")
    global active
    global global_cursors
    logger.debug("signal: message - isactive? " + active)
    if active == "false":
        sys.exit()
    else:
        opt_partition = str(i)
        global_use_instance_principal = config_items["global_use_instance_principal"]
        global_private_key = config_items["global_private_key"]
        global_private_key_password = config_items["global_private_key_password"]
        global_user_ocid = config_items["global_user_ocid"]
        global_tenancy_ocid = config_items["global_tenancy_ocid"]
        opt_stream_endpoint = config_items["opt_stream_endpoint"]
        opt_oci_region = config_items["opt_oci_region"]
        global_fingerprint = config_items["global_fingerprint"]
        stream_id = config_items["stream_id"]

        logger.debug("function: get_messages partition is: " + opt_partition)

        if cursor is None:
            cursor = get_cursor_by_group(global_stream_clients[i], stream_id, stream_id, opt_partition)
        try:
            get_response = global_stream_clients[i].get_messages(stream_id, cursor, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)

            logger.debug("function: get_messages get_response type is: " + str(get_response.headers))
            logger.debug("function: get_messages get_response status is: " + str(get_response.status))

            if not get_response.data:
                print("nodata")
                logger.debug("function: get_messages: No Data Returned")
                return None
            else:
                logger.debug("function: get_messages: Data Returned")

                return (get_response)

        except oci.exceptions.ServiceError as e:

            logger.debug("function: get_messages no cursor: " + str(e))

            if e.status == 429:
                message = e.message.split("next request can be made in ")
                message = message[1].split("ms")
                timer = (int(message[0]) / 1000)
                time.sleep((int(message[0]) / 1000))
                return ("429 Slow Down")
            elif e.status == 400:
                if e.message == "The cursor is expired. Create a new one.":
                    time.sleep(int(global_interval))
                    #global_cursors[str(i)] = get_cursor_by_group(global_stream_clients[i], stream_id, stream_id, opt_partition)
                    logger.debug(global_cursors[str(i)])
                    logger.debug(e.message)
                    return ("400 Cursor Expired")

                if e.message == "The cursor is invalid. Create a new one.":
                    time.sleep(int(global_interval))
                    #global_cursors[str(i)] = get_cursor_by_group(global_stream_clients[i], stream_id, stream_id, opt_partition)
                    logger.debug(global_cursors[str(i)])
                    logger.debug(e.message)
                    return ("400 Cursor Invalid")

                if e.message == "The cursor is outside the retention period and is now invalid.":
                    logger.debug(e.message)
                    update_details = oci.streaming.models.UpdateGroupDetails(type=oci.streaming.models.UpdateGroupDetails.TYPE_LATEST)
                    update = global_stream_clients[i].update_group(stream_id, stream_id, update_details, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
                    return ("400 Cursor Old")
            elif e.status == 404 or e.status == 401:
                logger.error("UNAUTHORIZED: This could be related to OCI IAM permissions.")
                sys.exit()
            else:
                logger.error("Unknown Error: " + str(e))
                time.sleep(int(global_interval))
                return ("Unknown Error")


def stop_process(signum, frame):
    global active
    active = "false"
    logger.debug("signal: stop process - isactive? " + active)
    logger.debug("term signal: " + str(signum) + " " + str(frame))
    sys.exit()


class Stream(Script):
    def __init__(self):
        pass

    def get_scheme(self):
        """This overrides the super method from the parent class"""
        scheme = Scheme("OCI Logging")
        scheme.description = "Splunk Modular Input for OCI Logging Streams"
        scheme.use_external_validation = True
        stream_id = Argument(
            name="stream_id",
            description="OCI Stream ID",
            data_type=Argument.data_type_string,
            required_on_edit=True,
            required_on_create=True
        )
        scheme.add_argument(stream_id)
        endpoint = Argument(
            name="stream_endpoint",
            description="Define field name to use as hostnames from the lookup file",
            data_type=Argument.data_type_string,
            required_on_edit=True,
            required_on_create=True
        )
        scheme.add_argument(endpoint)
        region = Argument(
            name="oci_region",
            description="OCI Region",
            data_type=Argument.data_type_string,
            required_on_edit=False,
            required_on_create=False
        )
        scheme.add_argument(region)

        private_key = Argument(
            name="private_key",
            description="Private Key",
            data_type=Argument.data_type_string,
            required_on_edit=False,
            required_on_create=False
        )
        scheme.add_argument(private_key)

        private_key_password = Argument(
            name="private_key_password",
            description="Private Key Password",
            data_type=Argument.data_type_string,
            required_on_edit=False,
            required_on_create=False
        )
        scheme.add_argument(private_key_password)

        user_ocid = Argument(
            name="user_ocid",
            description="User OCID",
            data_type=Argument.data_type_string,
            required_on_edit=False,
            required_on_create=False
        )
        scheme.add_argument(user_ocid)

        tenancy_ocid = Argument(
            name="tenancy_ocid",
            description="Tenancy OCID",
            data_type=Argument.data_type_string,
            required_on_edit=False,
            required_on_create=False
        )
        scheme.add_argument(tenancy_ocid)

        fingerprint = Argument(
            name="fingerprint",
            description="Fingerprint",
            data_type=Argument.data_type_string,
            required_on_edit=False,
            required_on_create=False
        )
        scheme.add_argument(fingerprint)

        use_instance_principal = Argument(
            name="use_instance_principal",
            description="Use Instance Principal",
            data_type=Argument.data_type_boolean,
            required_on_edit=False,
            required_on_create=False
        )
        scheme.add_argument(use_instance_principal)

        partition = Argument(
            name="partition",
            description="Define number of worker threads to use for this input",
            data_type=Argument.data_type_number,
            validation="is_pos_int('partition')",
            required_on_edit=False,
            required_on_create=False
        )
        scheme.add_argument(partition)

        message_limit = Argument(
            name="message_limit",
            description="Number of messages in each request",
            data_type=Argument.data_type_number,
            validation="is_pos_int('message_limit')",
            required_on_edit=False,
            required_on_create=False
        )
        scheme.add_argument(message_limit)

        proxy = Argument(
            name="proxy",
            description="https://myproxy:port",
            data_type=Argument.data_type_string,
            required_on_edit=False,
            required_on_create=False
        )
        scheme.add_argument(proxy)

        private_key_location = Argument(
            name="private_key_location",
            description="Private Key File Location",
            data_type=Argument.data_type_string,
            required_on_edit=False,
            required_on_create=False
        )
        scheme.add_argument(private_key_location)
        
        retry_interval = Argument(
            name="retry_interval",
            description="Retry Interval",
            data_type=Argument.data_type_number,
            required_on_edit=False,
            required_on_create=False
        )
        scheme.add_argument(retry_interval)

        

        return scheme

    def validate_input(self, definition):
        return

    def disable_input(self, input_name):
        global active
        active = "false"
        logger.debug("signal: disable input - isactive? " + active)
        self.service.inputs[input_name].disable()
        return

    def stream_events(self, inputs, ew):
        signal.signal(signal.SIGINT, stop_process)
        signal.signal(signal.SIGTERM, stop_process)
        signal.signal(signal.SIGHUP, stop_process)
        signal.signal(signal.SIGPIPE, stop_process)
        global active
        global global_interval
        global retries 
        self.input_name, self.input_item = inputs.inputs.popitem()
        global_interval = self.input_item["retry_interval"]
        logger.debug("function: stream events: entering stream_private_key type is: " + str(self.input_item["private_key"]))
        logger.debug("function: stream events: entering stream_private_key is: " + self.input_item["private_key"])

        global_use_instance_principal = self.input_item["use_instance_principal"]
        key = "private_key_password"
        global_proxy = None
        proxy_input = "proxy"
        if proxy_input in self.input_item.keys():
            global_proxy = self.input_item["proxy"]
            logger.debug("function: stream events: proxy server is: " + self.input_item["proxy"])
        if key in self.input_item.keys():
            global_private_key_password = self.input_item["private_key_password"]
        else:
            global_private_key_password = None
        opt_oci_region = self.input_item["oci_region"]
        stream_id = self.input_item["stream_id"]
        opt_stream_endpoint = self.input_item["stream_endpoint"]
        opt_partition = self.input_item["partition"]
        output_index = self.input_item["index"]
        logger.debug("function: stream_event opt_partition: " + opt_partition)
        thread_no = (int(opt_partition))
        for i in range(thread_no):
            logger.debug("function: stream_event: looping through partitions")
            logger.debug("function: stream_event: Building OCI Config")
            global_retries[str(i)] = 0

            ## Using Instance Principal
            if global_use_instance_principal == "True" or global_use_instance_principal == "1":
                logger.debug("function: stream_event: Using instance_principal")
                signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
                global_stream_clients[i] = oci.streaming.StreamClient(config={}, signer=signer, service_endpoint=opt_stream_endpoint)
                global_user_ocid = None
                global_tenancy_ocid = None
                global_fingerprint = None
                global_private_key = None
                global_private_key_password = None
                if not global_proxy:
                    pass
                else:
                    global_stream_clients[i].base_client.session.proxies = {'https': global_proxy}

            ## Using OCI API Key from Local Files system
            elif "private_key_location" in self.input_item.keys():
                logger.debug("function: stream_event: Using a file system API Key")

                global_private_key_location = self.input_item["private_key_location"]
                global_user_ocid = self.input_item["user_ocid"]
                global_tenancy_ocid = self.input_item["tenancy_ocid"]
                global_fingerprint = self.input_item["fingerprint"]
                global_private_key = self.input_item["private_key"]
                logger.debug("My Key file location is: " + global_private_key_location)

                if not(os.path.isfile(global_private_key_location)):
                    logger.error("ERROR: KEY FILE ON FILE SYSTEM DOES NOT Exist")
                    sys.exit()

                if global_private_key_password is None:
                    logger.debug("function: stream_event:  Using a file system API Key with no password")
                    config = {
                        "user": global_user_ocid,
                        "key_file": global_private_key_location,
                        "fingerprint": global_fingerprint,
                        "tenancy": global_tenancy_ocid,
                        "region": opt_oci_region
                    }
                else:
                    logger.debug("function: stream_event: Using a file system API Key with a password")

                    config = {
                        "user": global_user_ocid,
                        "key_file": global_private_key_location,
                        "fingerprint": global_fingerprint,
                        "tenancy": global_tenancy_ocid,
                        "region": opt_oci_region,
                        "pass_phrase": global_private_key_password,
                    }
                global_stream_clients[i] = oci.streaming.StreamClient(config, service_endpoint=opt_stream_endpoint)

                if not global_proxy:
                    pass
                else:
                    global_stream_clients[i].base_client.session.proxies = {'https': global_proxy}
                    logger.debug("function: stream_event: Global Proxy is set to for local file system API: " + global_proxy)

                logger.debug("function: stream_event: Stream Client Created for file system API Key")
            
            ## Using Uploaded OCI API Key
            elif "-----BEGIN RSA PRIVATE KEY-----" in self.input_item["private_key"]:
                logger.debug("function: stream_event: Using UI uploaded API Key")
                global_user_ocid = self.input_item["user_ocid"]
                global_tenancy_ocid = self.input_item["tenancy_ocid"]
                global_fingerprint = self.input_item["fingerprint"]
                global_private_key = self.input_item["private_key"]
                splitted = global_private_key.split('-----BEGIN RSA PRIVATE KEY-----')
                if len(splitted) != 2:
                    logger.error("Invalid API Key, must be an RSA Key. Spiltted: " + str(len(splitted)))
                    exit()
                replaced = splitted[1]
                private_key = ("-----BEGIN RSA PRIVATE KEY-----" + replaced[:-2]).replace('\\n', '\n')
                WINDOWS_LINE_ENDING = '\r\n'
                UNIX_LINE_ENDING = '\n'
                private_key = private_key.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

                if global_private_key_password is None:
                    logger.debug("function: stream_event: API Key is not using a password")

                    config = {
                        "user": global_user_ocid,
                        "key_content": private_key,
                        "fingerprint": global_fingerprint,
                        "tenancy": global_tenancy_ocid,
                        "region": opt_oci_region
                    }

                else:
                    logger.debug("function: stream_event: Using API Key Password")

                    config = {
                        "user": global_user_ocid,
                        "key_content": private_key,
                        "fingerprint": global_fingerprint,
                        "tenancy": global_tenancy_ocid,
                        "region": opt_oci_region,
                        "pass_phrase": global_private_key_password,
                    }

                global_stream_clients[i] = oci.streaming.StreamClient(config, service_endpoint=opt_stream_endpoint)

                if not global_proxy:
                    pass
                else:
                    global_stream_clients[i].base_client.session.proxies = {'https': global_proxy}
                    logger.debug("function: stream_event: Global Proxy is set to for uploaded API: " + global_proxy)

                logger.debug("function: stream_event: Stream Client Created for Uploaded API Key")

            else:
                logger.error("NO VALID AUTHENTICATION METHOD FOUND")
                sys.exit()
            global global_cursors
            global_cursors[str(i)] = None

        if thread_no > 0:
            logger.debug("function: stream_event: Executing Threads")
            pool = mp.Pool(processes=thread_no)
            while True:
                try:
                    
                    config_items = {
                        "global_use_instance_principal": global_use_instance_principal,
                        "global_private_key": global_private_key,
                        "global_private_key_password": global_private_key_password,
                        "global_user_ocid": global_user_ocid,
                        "global_tenancy_ocid": global_tenancy_ocid,
                        "opt_stream_endpoint": opt_stream_endpoint,
                        "opt_oci_region": opt_oci_region,
                        "global_fingerprint": global_fingerprint,
                        "stream_id": stream_id
                    }
                    logger.debug("signal: multi process - isactive? " + active)
                    TASKS = [(config_items, global_cursors[str(i)], i) for i in range(thread_no)]
                    results = [pool.apply_async(get_messages, t) for t in TASKS]
                    posi = 0
                    logger.debug("Stream events: Start Posi is: " + str(posi))
                    if isinstance(results, str):
                        logger.debug(str(results))
                        errors = ["400 Cursor Invalid","400 Cursor Expired","400 Cursor Old", "Unknown Error"]
                        if any(x in results for x in errors):
                            logger.debug("function: stream_event 400 is: " + str(x))
                        errors = ["429 Slow Down"]
                        if any(x in results for x in errors):
                            logger.debug("function: stream_event 429 Slow Down is: " + str(x))
                    elif isinstance(results, int):
                        logger.debug("function: stream_event result is: No messages")
                        time.sleep(global_interval)
                    else:
                        for r in results:
                            logger.debug("function: stream_event: result is: " + str(r))    
                            logger.debug("function: stream_event: Start of results loop Posi is: " + str(posi))
                            get_response = r.get()
                            errors = ["400 Cursor Invalid","400 Cursor Expired","400 Cursor Old", "Unknown Error"]
                            logger.debug("function: stream_event get_response is: " + str(get_response))
                            if get_response is not None:
                                get_response_str = str(get_response)
                                logger.debug("function: stream_event get_response has data: " + str(get_response))
                                logger.debug("function: stream_event: With data of results loop Posi is: " + str(posi))
                                if any(x in get_response_str for x in errors):
                                    global_retries[str(posi)] = global_retries[str(posi)] + 1
                                    logger.debug("Stream events: With Errors of results loop Posi is: " + str(posi))
                                    global_cursors[str(i)] = get_cursor_by_group(global_stream_clients[i], stream_id, stream_id, str(posi))
                                    logger.debug("function: stream_event: With data of post cursor loop Posi is: " + str(posi))
                                    if int(global_retries[str(posi)]) == int(retries):
                                        ew.log("2","Cursor not valid or no data")
                                        global_retries[str(posi)] = 0 
                                if hasattr(get_response, 'data'):
                                    for message in get_response.data:
                                        data = b64decode(message.value.encode().decode()).decode("utf-8")
                                        if data:
                                            try:
                                                y = json.loads(data)
                                                if 'subject' in y:
                                                    host = y["subject"]
                                                else:
                                                    host = y["oracle"]["compartmentid"]
                                                logevent = Event(data=data, time=y["time"], host=host, index=output_index, done=True, unbroken=True)
                                                ew.write_event(logevent)
                                                logger.debug("function: stream_event: Wrote Event to Splunk")
                                                global_cursors[str(posi)] = get_response.headers["opc-next-cursor"]
                                                global_retries[str(posi)] = 0 
                                            except Exception as e:
                                                logger.info("function: stream_event: Unsupported Record: " + str(data))
                            posi = posi + 1
                            logger.debug("function: stream_event: End of for R Posi is: " + str(posi))
                except Exception as e:
                    logger.debug("function: stream_event: pool exception: " + str(e))
                    pool.close()
                    pool.join()
                    track = traceback.format_exc()
                    sys.stderr.write(str(track))
                    return


if __name__ == "__main__":
    sys.exit(Stream().run(sys.argv))
