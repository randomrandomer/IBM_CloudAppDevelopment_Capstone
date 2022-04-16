// Get all dealerships, and all dealerships for a specific state

function main(params) {

    secret={
        "COUCH_URL":"https://ec46d1dc-cbdb-4bed-9b11-7e187c85c738-bluemix.cloudantnosqldb.appdomain.cloud",
        "IAM_API_KEY":"2b7X2252IJ1hA0Lu1jDdt4egXVQ6cRiDRjIJ8CEz1817",
        "COUCH_USERNAME":"ec46d1dc-cbdb-4bed-9b11-7e187c85c738-bluemix"
    };

    console.log(params);

    return new Promise(function (resolve, reject) {
        const Cloudant = require('@cloudant/cloudant');
        const cloudant = Cloudant({
            url: secret.COUCH_URL,
            plugins: {iamauth: {iamApiKey:secret.IAM_API_KEY}}
        });

        const dealershipDb = cloudant.use('dealerships');

        if (params.state) {
            // Return all dealerships with this state

            dealershipDb.find({

                "selector": {
                    "state": {
                        "$eq": params.state
                    }
                }
            }, function (err, result) {

                if (err) {
                    console.log("Error finding dealerships with state", err)
                    reject(err);
                }

                let code=200;

                if (result.docs.length == 0)
                {
                    code = 404;
                }
                resolve({
                    statusCode: code,
                    headers: { 'Content-Type': 'application/json' },
                    body: result
                });
            });
        } else if (params.id) {

            // id = parseInt(params.dealerId)

            // dealershipDb.find({selector: {id:parseInt(params.id)}}, function (err, results) {
            //     if (err) {
            //         console.log("Error finding dealerships by id", err)
            //         reject(err);
            //     }

            //     let code = 200;

            //     if (result.docs.length==0)
            //     {
            //         code = 404;
            //     }

            //     resolve({
            //         statusCode: code,
            //         headers: { 'Content-Type': 'application/json' },
            //         body: result
            //     });

            dealershipDb.find({

                "selector": {
                    "id": {
                        "$eq": params.id
                    }
                }
            }, function (err, result) {

                if (err) {
                    console.log("Error finding dealerships with id", err)
                    reject(err);
                }

                let code=200;

                if (result.docs.length == 0)
                {
                    code = 404;
                }
                resolve({
                    statusCode: code,
                    headers: { 'Content-Type': 'application/json' },
                    body: result
                });

            });
        } else {
            // Return all documents

            dealershipDb.list({ include_docs: true}, function (err, result) {
                if (err) {
                    console.log("Error retrieving all dealerships", err)
                    reject(err);
                }
                resolve({
                    statusCode: 200,
                    headers: { 'Content-Type': 'application/json' },
                    body: result
                });
            });
        }
    });
}