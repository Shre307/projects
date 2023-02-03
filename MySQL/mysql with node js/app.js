var mysql = require('mysql');
var faker = require('faker');

var connection = mysql.createConnection({
    host: 'localhost',
    user: 'shre',
    password: 'Kmno4kmno',
    database: 'join_us'
});

//selecting data===============================================================
// var q = 'select count(*) from users as total';
// connection.query(q, function(error, results, fields) {
//     if (error) throw error;
//     console.log(results);
// });

//Inserting data===============================================================
// var q = 'Insert into users(email) values ("wasty_the_dog@gmail.com")';
// connection.query(q, function(error, results, fields) {
//     if (error) throw error;
//     console.log(results);
// });

//INserting data take-2=======================================================
// var person = {
//     email: faker.internet.email(),
//     created_at: faker.date.past()
// };

// console.log(person);

// var end_result = connection.query('insert into users set ?', person, function(err, result) {
//     if (err) throw err;
//     console.log(result);
// })

// connection.end();


//Inserting Lots of data ======================================================

var data = [];
for (var i = 0; i < 500; i++) {
    data.push([
        faker.internet.email(),
        faker.date.past()
    ]);
}
// console.log(data);

var q = 'insert into users (email, created_at) values ?';

connection.query(q, [data], function(err, result) {
    console.log(err);
    console.log(result);
})

connection.end();