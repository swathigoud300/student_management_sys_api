import requests
import json
import jsonpath

def test_add_student():
    url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("C:\\Users\\tiruk\\Add_student.json",'r')
    json_request = json.loads(file.read())
    response = requests.post(url,json_request)
    print(response.text)
    """print(response.content)
    print(response.headers)
    print(response.headers.get('Location'))"""


def test_add_student():
    url = "https://thetestingworldapi.com/api/studentsDetails/2684427"
    response = requests.get(url)
    print(response.text)
    json_response = json.loads(response.text)
    first_name = jsonpath.jsonpath(json_response,'data.first_name')
    print(first_name)


def test_update_student():
    url = "https://thetestingworldapi.com/api/studentsDetails/2684427"
    file = open("C:\\Users\\tiruk\\Update_student.json")
    json_input = file.read()
    json_request = json.loads(json_input)
    response = requests.put(url,json_request)
    print(response.text)
    json_response = response.json()
    print(json_response)
    id = jsonpath.jsonpath(json_response,'data.id')
    print(id)













