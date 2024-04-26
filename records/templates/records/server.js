const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');

const app = express();
const port = 3000;

// Configure MySQL connection
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'new_password',
  database: 'ipamsdjango'
});

// Connect to MySQL
connection.connect((err) => {
  if (err) {
    console.error('Error connecting to MySQL:', err);
    return;
  }
  console.log('Connected to MySQL');
});

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Endpoint to handle incoming chat queries
app.post('/query', (req, res) => {
  const { message } = req.body;
  
  // Process the message here using NLP libraries
  // For simplicity, we'll assume the message contains a raw SQL query
  
  // Execute the SQL query
  connection.query(message, (error, results, fields) => {
    if (error) {
      console.error('Error executing SQL query:', error);
      res.status(500).json({ error: 'Internal Server Error' });
      return;
    }
    // Assuming successful execution, send back the results
    res.json({ results });
  });
});

const express = require('express');
const app = express();

// Enable CORS middleware
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', 'http://127.0.0.1:8000');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    next();
});

// Your route handlers
app.get('/', (req, res) => {
    res.send('Hello from Express!');
});

// Start the server
app.listen(8000, () => {
    console.log('Server is running on port 8000');
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
