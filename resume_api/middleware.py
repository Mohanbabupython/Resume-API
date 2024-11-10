#By using Middleware to creating for Logfiles along with current date..
import datetime
import os
import pandas as pd
from datetime import datetime
import traceback
from django.utils.deprecation import MiddlewareMixin

current_dir = os.getcwd()
log_path = os.path.join(current_dir, 'LogFiles')
if not os.path.exists(log_path):
    os.makedirs(log_path, exist_ok=True)

class CustomLogMiddleware(MiddlewareMixin):
    def custom_logging(self, request, response):
        try:
            response_body = response.data
        except:
            response_body = {}
        
        log_data = {
            "start_time      :": request.start_time,
            "end_time        :": request.end_time,      
            "run_time        :": (request.end_time - request.start_time).total_seconds(),
            "request_body    :": request.payload,
            "response_body   :": response_body,
            "request_method  :": request.method,
            "status_code     :": response.status_code,
            "request path    :": request.path,
            "-----------------------------------------------" : "-----------------------------------------------------"
        }

        log_file = 'Api_log_' + str(datetime.now().strftime('%Y-%m-%d')) + '.txt'
        df = pd.DataFrame.from_dict(log_data, orient='index')
        df.to_csv(os.path.join(log_path, log_file), mode="a", header=False, sep='\t')

    def process_request(self, request):
        request.start_time = datetime.now()
        try:
            if request.method != 'GET':
                data = request.body.decode("utf-8") if request.body else None
            else:
                data = None
            request.payload = data if data else None
        except Exception as e:
            traceback.print_exc()
            request.payload = None

    def process_response(self, request, response):
        request.end_time = datetime.now()
        self.custom_logging(request, response)
        return response
