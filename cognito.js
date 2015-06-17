var AWS = require('aws-sdk');
var awsRegion = "us-east-1";
var cognitoParams = {
    AccountId: "AWSアカウントID",
    RoleArn: "arn:aws:iam::AWSアカウントID:role/Cognito_SensorHUBUnauth_Role",
    IdentityPoolId: "us-east-1:AWSのIdentityのPoolId"
};

AWS.config.region = awsRegion;
AWS.config.credentials = new AWS.CognitoIdentityCredentials(cognitoParams);
AWS.config.credentials.get(function(err) {
        if (!err) {
            console.log("Cognito Identity Id: " + AWS.config.credentials.identityId);
        }
});
