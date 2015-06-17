var execSync = require('child_process').execSync;
var id = "Hub01";

var AWS = require('aws-sdk');
var awsRegion = "us-east-1";

// 1タイムアクセスID取得
var cognitoParams = {
    AccountId: "AWSアカウントID",
    RoleArn: "arn:aws:iam::AWSアカウントID:role/Cognito_SensorHUBUnauth_Role",
    IdentityPoolId: "us-east-1:AWSのIdentityのPoolId"
};
AWS.config.region = awsRegion;
AWS.config.credentials = new AWS.CognitoIdentityCredentials(cognitoParams);
AWS.config.credentials.get(function(err) {
    if (!err) {
//        console.log("Cognito Identity Id: " + AWS.config.credentials.identityId);
    }
});

var s3 = new AWS.S3();
var bucket = 's.ykata.net';
// センサ値取得
var result = "" + execSync('sudo /home/pi/getSensor.py');

// 現在値をJSONでS3にアップ
var vRes  = result.replace(/[\n\r]/g,"").split(",");
var vKeyN = id + "/now.json";
var vKeyF = vRes[0].replace(/\//g,"_");
var vKeyD = id + "/" + vKeyF + ".json";
var vJson = '{"Date":"'+vRes[0]+'","Time":"'+vRes[1]+'","Temperature":'+vRes[2]+',';
vJson = vJson + '"Humidity":'+vRes[3]+',"CO2":'+vRes[4]+',"Illuminance":'+vRes[5]+'}';
var params1 = {
    Bucket: bucket,
    Key: vKeyN,
    ContentType: 'application/json',
    Body: vJson
};
s3.upload(params1, function(err) {
    if(err) {
        console.log("Error uploading data 01 : ", err);
    }
});

//  1日のデータをファイルに保管し、JSONでS3にアップ
var fs = require('fs');
var path = './'+vKeyF;
var fsData = "";
var fsUPData = "";
try { 
    fs.statSync(path);
    fsData = fs.readFileSync(path, 'utf8');
    fsUPData = fsData + "," + vJson;
} catch (e) {
    execSync('echo "" >> ' + path);
    execSync('chmod 666 ' + path);
    fsUPData = vJson;
}
fs.writeFileSync(path, fsUPData,'utf8');
var params2 = {
    Bucket: bucket, 
    Key: vKeyD,
    ContentType: 'application/json',
    Body: '[' + fsUPData + ']'
}; 
s3.upload(params2, function(err) {
    if(err) {
        console.log("Error uploading data 02 : ", err);
    }
});
