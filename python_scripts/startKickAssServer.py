import uhttpd
import uhttpd.file_handler
server = uhttpd.Server([('/', uhttpd.file_handler.Handler('/www'))])
server.run()
