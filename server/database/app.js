const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const  cors = require('cors')
const app = express()
const port = 3030;

app.use(cors())
app.use(require('body-parser').urlencoded({ extended: false }));

const reviews_data = JSON.parse(fs.readFileSync("reviews.json", 'utf8'));
const dealerships_data = JSON.parse(fs.readFileSync("dealerships.json", 'utf8'));

mongoose.connect("mongodb://mongo_db:27017/",{'dbName':'dealershipsDB'});


const Reviews = require('./review');

const Dealerships = require('./dealership');

try {
  Reviews.deleteMany({}).then(()=>{
    Reviews.insertMany(reviews_data['reviews']);
  });
  Dealerships.deleteMany({}).then(()=>{
    Dealerships.insertMany(dealerships_data['dealerships']);
  });
  
} catch (error) {
  res.status(500).json({ error: 'Error fetching documents' });
}


// Express route to home
app.get('/', async (req, res) => {
    res.send("Welcome to the Mongoose API")
});

// Express route to fetch all reviews
app.get('/fetchReviews', async (req, res) => {
  try {
    const documents = await Reviews.find();
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to fetch reviews by a particular dealer
app.get('/fetchReviews/dealer/:id', async (req, res) => {
  try {
    const documents = await Reviews.find({dealership: req.params.id});
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to fetch all dealerships
app.get('/fetchDealers', async (req, res) => {
    try {
      const dealerships = await Dealerships.find(); // Fetch all dealerships
      if (dealerships.length === 0) {
        return res.status(404).json({ message: 'No dealerships found' });
      }
      res.status(200).json(dealerships);
    } catch (error) {
      console.error('Error fetching dealerships:', error);
      res.status(500).json({ error: 'An error occurred while fetching dealerships' });
    }
  });
  
  // Express route to fetch dealerships by a particular state
  app.get('/fetchDealers/:state', async (req, res) => {
    try {
      const state = req.params.state;
      const dealerships = await Dealerships.find({ state }); // Filter dealerships by state
      if (dealerships.length === 0) {
        return res.status(404).json({ message: `No dealerships found in state: ${state}` });
      }
      res.status(200).json(dealerships);
    } catch (error) {
      console.error(`Error fetching dealerships for state: ${req.params.state}`, error);
      res.status(500).json({ error: `An error occurred while fetching dealerships for state: ${req.params.state}` });
    }
  });
  
  // Express route to fetch a dealership by a particular ID
  const mongoose = require('mongoose');

// Express route to fetch a dealership by a particular ID
app.get('/fetchDealer/:id', async (req, res) => {
  try {
    const id = req.params.id;

    // Check if the ID is a valid ObjectId
    if (!mongoose.Types.ObjectId.isValid(id)) {
      return res.status(400).json({ error: 'Invalid dealership ID format' });
    }

    const dealership = await Dealerships.findById(id); // Fetch dealership by ID

    if (!dealership) {
      return res.status(404).json({ message: 'Dealer not found' });
    }
    res.status(200).json(dealership);
  } catch (error) {
    console.error('Error fetching dealership by ID:', error);
    res.status(500).json({ error: 'An error occurred while fetching dealership by ID' });
  }
});

//Express route to insert review
app.post('/insert_review', express.raw({ type: '*/*' }), async (req, res) => {
  data = JSON.parse(req.body);
  const documents = await Reviews.find().sort( { id: -1 } )
  let new_id = documents[0]['id']+1

  const review = new Reviews({
		"id": new_id,
		"name": data['name'],
		"dealership": data['dealership'],
		"review": data['review'],
		"purchase": data['purchase'],
		"purchase_date": data['purchase_date'],
		"car_make": data['car_make'],
		"car_model": data['car_model'],
		"car_year": data['car_year'],
	});

  try {
    const savedReview = await review.save();
    res.json(savedReview);
  } catch (error) {
		console.log(error);
    res.status(500).json({ error: 'Error inserting review' });
  }
});

// Start the Express server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
