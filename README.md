# IOT Connect Reply MicroService

## Prerequisites

To deploy the https endpoint alongside microservice, you will need to have AWS SAM CLI and python installed. If you haven't installed it yet, follow the instructions below.

### Installing Dependencies

-  Install AWS SAM CLI: To install AWS SAM CLI please refer to the official AWS SAM CLI documentation [here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

- Install Python

## Getting Started

Follow these steps to deploy and run the application:
1. Navigate to the project directory:
2. Execute the following commands and pass the desired password as a parameter:
```bash
cd scripts
.\store_api_pass mysupersecurepass
```
Note: You must pass this password in your headers to the api call with header name: Auth-Pass

3. Open the `template.yaml` file and update the following Parameter in as per your requirements:
    - `REDIRECT_URL`: Set it to the desired website link. 
4. The default region of deployment is set to be `us-east-1` in samconfig.toml. Please change that as required.
5. Build and deploy the application using the following command:
```bash
sam sync
```
6. Go to Api Gateway console. Click on `Api-->AwsApiGateway-->Api Keys-->Api`
    - Click on show key and note it down. You must pass this key as `x-api-key   header
