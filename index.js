const Realm = require('realm')
// const schema = require('./CloudRealm');
const schema = require('./CloudRealmAdmin');

// let adminUser = 'alex';
// let adminPass = 'alex';
let adminUser = 'admindemobsc';
let adminPass = 'V4zPU8FjL6kAf_X';
const authUrl = 'https://demobsc.us1a.cloud.realm.io';
// let creds = Realm.Sync.Credentials.usernamePassword(adminUser, adminPass,true);

let creds = Realm.Sync.Credentials.usernamePassword(adminUser, adminPass);

const configuration = {
    // sync: {
    //   fullSynchronization: true,
    //   url: 'realms://demobsc.us1a.cloud.realm.io/TestRoles'
    //   // url: 'realms://demobsc.us1a.cloud.realm.io/~/myRealm'
    // },
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
    // console.log(user.isAdmin)
    const realm = new Realm(config);
    let roles = realm.objects(Realm.Permissions.Role);
    console.log(JSON.stringify(roles,null,4))
    // let role = realm.create(Realm.Permissions.Role, {name: 'mytest-role'})

    // console.log(JSON.stringify(realm,null,4))

        // Realm.open(config).then((realm) => {
        //   try{
        //     let role = realm.create(Realm.Permissions.Role,{name: 'test-role'});
        //     let userid = user.identity;
            
        //     // let roles = realm.objects(Realm.Permissions.Role);
        //     // console.log(JSON.stringify(realm.permissions,null,4))
        //     // realm.write(() => {
        //     //   realm.create(Realm.Permissions.Role, { name: "role-info-app" });
        //     // });
        //   }catch(e){
        //     console.log('error create: '+e.message)
        //   }
        //   // let roles = realm.objects(Realm.Permissions.Role);
        //   // console.log(JSON.stringify(roles,null,4))
        //   // console.log(JSON.stringify(realm,null,4))
        // }).catch(error =>{
        //     console.log(JSON.stringify('error => ' + error.message,null,4))
        // });

}).catch(error => {
    console.log(JSON.stringify('error => : '+error,null,4))
})
