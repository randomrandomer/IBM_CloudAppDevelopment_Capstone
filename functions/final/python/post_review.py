import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def main(dict):
    authenticator = IAMAuthenticator('2b7X2252IJ1hA0Lu1jDdt4egXVQ6cRiDRjIJ8CEz1817')
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://ec46d1dc-cbdb-4bed-9b11-7e187c85c738-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_document(db='reviews', document=dict["review"]).get_result()
    try:
        result = {
            'headers': {'Content-Type': 'application/json'},
            'body': {'data': response}
        }
        return result
    except:
        return {
            'statusCode': 404,
            'message': 'Something went wrong'
        }