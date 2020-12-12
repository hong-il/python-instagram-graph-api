"""
    @ Author    : hong-il
    @ Date      : 2020-12-12
    @ File name : define.py
    @ File path :
    @ Description :
"""

import requests
import json


def getCreds():
    creds = dict()  # dictionary to hold everything
    creds['access_token'] = 'EAAC6AHSI8pQBADd00EXQU8s3pkemh8jLj4sFIV933zaXgCg0d9vxhmB5xXshsWAuHKWb3lyk47FVlysTPlgwDHtVhCB3vmMsOgjqpB8a87okO9ElLFK1S9dVENYFaZBOwSQaOpzRLyvW1MEMRggML3k8fCLyQm8jDB8ZAXonGKP4jTScmFnaeAHuSxBA7rbZAkTp3leoUV3QVuLVT0m5EBPHvj7qFPyYGRIXzxkhBO26Gl6yZBBZC'  # access token for use with all api calls
    creds['client_id'] = '204511117898388'  # client id from facebook app IG Graph API Test
    creds['client_secret'] = 'd035a5657809e25debb3f437574462a7'  # client secret from facebook app
    creds['graph_domain'] = 'https://graph.facebook.com/'  # base domain for api calls
    creds['graph_version'] = 'v7.0'  # version of the api we are hitting
    creds['endpoint_base'] = creds['graph_domain'] + creds[
        'graph_version'] + '/'  # base endpoint with domain and version
    creds['debug'] = 'no'  # debug mode for api call
    creds['page_id'] = 'your-page-id'  # users page id after running the "get_user_facebook_page.py"
    creds[
        'instagram_account_id'] = 'your-instagram-id'  # users instagram account id after running the "get_user_instagram_page.py"
    creds['ig_username'] = 'imakashsahu'  # ig username to get details

    return creds


def makeApiCall(url, endpointParams, debug='no'):
    data = requests.get(url, endpointParams)  # make get request

    response = dict()  # hold response info
    response['url'] = url  # url we are hitting
    response['endpoint_params'] = endpointParams  # parameters for the endpoint
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent=4)  # pretty print for cli
    response['json_data'] = json.loads(data.content)  # response data from the api
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)  # pretty print for cli

    if ('yes' == debug):  # display out response info
        displayApiCallData(response)  # display response

    return response  # get and return content


def displayApiCallData(response):
    """ Print out to cli response from api call """

    print("\nURL: ")  # title
    print(response['url'])  # display url hit
    print("\nEndpoint Params: ")  # title
    print(response['endpoint_params_pretty'])  # display params passed to the endpoint
    print("\nResponse: ")  # title
    print(response['json_data_pretty'])  # make look pretty for cli
