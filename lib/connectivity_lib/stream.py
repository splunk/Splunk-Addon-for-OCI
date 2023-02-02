from string import Template
from exceptions import *
import oci

event_message = Template('$timenow ,action=$action,status=$status_code,src=splunk,dst_hostname=$dsthost,'
                         'dst_ip=$dstip,description=$description')


def stream(stream_client,stream_id):

    try:
            
        get_response = stream_client.get_messages(stream_id, \
                            cursor,\
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
        helper.log_debug(get_response.data)
            

        if not get_response.data:
            helper.log_debug("nodata-" + filepath)

    except oci.exceptions.ServiceError as e:
        helper.log_error(e)
        if e.status == 429:
                #validate or pull from body
                #if get_response.headers["retry-after"]:
            message = e.message.split("next request can be made in ")
            message = message[1].split(" ms")
            timer = (int(message[0]) / 1000)
            time.sleep((int(message[0]) / 1000))
                
        if e.status == 400:
                # Read Body
                if e.message == "The cursor is expired. Create a new one.":
                    cursor = get_cursor_by_group(stream_client, stream_id, stream_id, opt_partion)
                    
                if e.message == "The cursor is invalid. Create a new one.":
                    cursor = get_cursor_by_group(stream_client, stream_id, stream_id, opt_partition)
                    
                if e.message == "The cursor is outside the retention period and is now invalid.":
                    update_details = oci.streaming.models.UpdateGroupDetails(type=oci.streaming.models.UpdateGroupDetails.TYPE_LATEST)
                    update = stream_client.update_group(stream_id, stream_id, update_details, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
        

    
    count=0
    for message in get_response.data:
        count= count + 1
        data=b64decode(message.value.encode().decode()).decode("utf-8")
        if data:
            try:
                y = json.loads(data)
                    
                if 'subject' in y:
                    host = y["subject"]
                else:
                    host = y["oracle"]["compartmentid"]
                #cursor = get_response.headers["opc-next-cursor"]
                return event_message.substitute(str(data), time=y["time"], host=host, index=output_index, source=y["source"], sourcetype=y["type"], done=True, unbroken=True)
                
            
            except Exception as e:
                helper.log_error(e)
        


