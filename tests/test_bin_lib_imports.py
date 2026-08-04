"""Smoke tests for the bin/lib vendored-dependency import chain.

Mirrors the manual verification used to confirm the bin/ -> bin/lib/
vendoring migration (and the later cffi/pycparser removal) don't break
anything, so future dependency bumps get the same coverage automatically
instead of relying on someone re-running that check by hand.

Runs against whichever CPython this test process is executed under -- CI
matrices this across the OS/Python combinations the add-on claims to
support (see BUILD.md).
"""
import os
import py_compile
import sys
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIN_DIR = os.path.join(REPO_ROOT, "bin")
LIB_DIR = os.path.join(BIN_DIR, "lib")

# Mirrors the sys.path.insert done by bin/oci_logging.py itself, before any
# of the vendored packages below are imported.
sys.path.insert(0, LIB_DIR)


class SplunklibSixRedirectFinder:
    """Copied verbatim from bin/oci_logging.py.

    splunklib vendors its own six.py that only implements the old PEP 302
    find_module/load_module protocol, which Python 3.12+ stops invoking.
    Without this, `import splunklib.client` raises ModuleNotFoundError for
    splunklib.six.moves.* under 3.12+. oci_logging.py registers this same
    finder before importing splunklib -- replicated here so the test
    reflects real behavior instead of a test-only import ordering gap.
    """

    def find_spec(self, fullname, path, target=None):
        if fullname.startswith("splunklib.six"):
            global_name = fullname.replace("splunklib.six", "six", 1)
            try:
                mod = sys.modules.get(global_name)
                if not mod:
                    __import__(global_name)
                    mod = sys.modules[global_name]
                sys.modules[fullname] = mod
                return getattr(mod, "__spec__", None)
            except Exception:
                pass
        return None


sys.meta_path.insert(0, SplunklibSixRedirectFinder())


class VendoredThirdPartyImportsTestCase(unittest.TestCase):
    def test_core_third_party_imports(self):
        import oci  # noqa: F401
        import multiprocess  # noqa: F401
        import certifi  # noqa: F401
        import cryptography  # noqa: F401
        import OpenSSL.SSL  # noqa: F401
        import OpenSSL.crypto  # noqa: F401
        import six  # noqa: F401
        import pytz  # noqa: F401
        import dateutil.parser  # noqa: F401
        import circuitbreaker  # noqa: F401
        import dill  # noqa: F401

    def test_oci_sdk_submodules_used_by_oci_logging(self):
        import oci.streaming.models  # noqa: F401
        import oci.auth.signers  # noqa: F401
        import oci.exceptions  # noqa: F401
        import oci.retry  # noqa: F401


class FirstPartyLibImportsTestCase(unittest.TestCase):
    def test_splunklib_and_connectivity_lib_import(self):
        import splunklib.client  # noqa: F401
        # Also pulls in bin/lib/constants.py and bin/lib/exceptions.py,
        # which connectivity_lib itself imports as bare top-level modules.
        import connectivity_lib.stream  # noqa: F401


class CryptographyFunctionalTestCase(unittest.TestCase):
    def test_sha256_digest(self):
        from cryptography.hazmat.primitives import hashes

        digest = hashes.Hash(hashes.SHA256())
        digest.update(b"ci-smoke-test")
        self.assertEqual(len(digest.finalize()), 32)


class PyOpenSSLFunctionalTestCase(unittest.TestCase):
    def test_rsa_keygen_and_tls_context(self):
        import OpenSSL.crypto
        import OpenSSL.SSL

        key = OpenSSL.crypto.PKey()
        key.generate_key(OpenSSL.crypto.TYPE_RSA, 2048)
        self.assertEqual(key.bits(), 2048)

        ctx = OpenSSL.SSL.Context(OpenSSL.SSL.TLS_METHOD)
        self.assertIsNotNone(ctx)


class EntrypointCompilesTestCase(unittest.TestCase):
    def test_oci_logging_py_compiles(self):
        entrypoint = os.path.join(BIN_DIR, "oci_logging.py")
        py_compile.compile(entrypoint, doraise=True)


if __name__ == "__main__":
    unittest.main()
