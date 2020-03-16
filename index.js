const Realm = require('realm')
// const schema = require('./CloudRealm');
const schema = require('./CloudRealmTickets');

let adminUser = 'alex';
let adminPass = 'alex';
// let adminUser = 'admindemobsc';
// let adminPass = 'V4zPU8FjL6kAf_X';
const authUrl = 'https://demobsc.us1a.cloud.realm.io';
// let creds = Realm.Sync.Credentials.usernamePassword(adminUser, adminPass,true);

let creds = Realm.Sync.Credentials.usernamePassword(adminUser, adminPass);

const configuration = {
    sync: {
      fullSynchronization: true,
      url: 'realms://demobsc.us1a.cloud.realm.io/~/myRealm'
    },
    schema
  };

// Realm.Sync.User.login(authUrl,creds).then(user => {
//   // if(user){
//   //   console.log('Usuario creado')
//   // }
//   // else{
//   //   console.log('Error al crear')
//   // }
//   console.log(JSON.stringify(user,null,4))
// }).catch(reason => {
//   console.log('Error:  '+ JSON.stringify(reason,null,4))
// })
  
Realm.Sync.User.login(authUrl, creds).then(user => {
    let config = user.createConfiguration(configuration);
        Realm.open(config).then((realm) => {
        }).catch(error =>{
            console.log(JSON.stringify('error => ' + error.message,null,4))
        });

}).catch(error => {
    console.log(JSON.stringify('error => : '+error,null,4))
})
