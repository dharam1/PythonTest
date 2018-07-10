import json
with open('data') as json_file:
    parse = json.load(json_file)
print(parse["Records"][0]["s3"]["bucket"]["arn"])