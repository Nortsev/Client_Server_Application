# if len(sys.argv) > 1:
#     for i in range(1, len(sys.argv)):
#         if sys.argv[i] == '-p' and i + 1 < len(sys.argv):
#             config.server_port = sys.argv[i + 1]
#         if sys.argv[i] == '-a' and i + 1 < len(sys.argv):
#             config.server_address = sys.argv[i + 1]

import config, sys
for i in range(1, len(sys.argv)):
    if sys.argv[i] == '-p' and i + 1 < len(sys.argv):
        config.server_port = sys.argv[i + 1]
        print(config.server_port)
    if sys.argv[i] == '-a' and i + 1 < len(sys.argv):
        config.server_address = sys.argv[i + 1]
        print(config.server_address)
