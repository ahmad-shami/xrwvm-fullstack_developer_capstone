// Import required modules
/*jshint esversion: 8 */
const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const cors = require('cors');

const app = express();
const port = 3030;

// Middleware
app.use(cors());
app.use(express.json());

// Load data
const reviewsData = JSON.parse(fs.readFileSync('reviews.json', 'utf8'));
const dealershipsData = JSON.parse(fs.readFileSync('dealerships.json', 'utf8'));

// Connect to MongoDB
mongoose.connect('mongodb://mongo_db:27017/', { 
  dbName: 'dealershipsDB', 
  useNewUrlParser: true, 
  useUnifiedTopology: true
});

// Import models
const Reviews = require('./review');
const Dealerships = require('./dealership');

// Populate database
(async () => {
  try {
    await Reviews.deleteMany({});
    await Reviews.insertMany(reviewsData.reviews);

    await Dealerships.deleteMany({});
    await Dealerships.insertMany(dealershipsData.dealerships);
  } catch (error) {
    console.error('Error populating database:', error);
  }
})();

// Routes
app.get('/', (req, res) => {
  res.send('Welcome to the Mongoose API');
});

app.get('/fetchReviews', async (req, res) => {
  try {
    const documents = await Reviews.find();
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

app.get('/fetchReviews/dealer/:id', async (req, res) => {
  try {
    const documents = await Reviews.find({ dealership: req.params.id });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

app.get('/fetchDealers', async (req, res) => {
  try {
    const dealerships = await Dealerships.find();
    if (dealerships.length === 0) {
      return res.status(404).json({ message: 'No dealerships found' });
    }
    res.status(200).json(dealerships);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealerships' });
  }
});

app.get('/fetchDealers/:state', async (req, res) => {
  try {
    const state = req.params.state;
    const dealerships = await Dealerships.find({ state });
    if (dealerships.length === 0) {
      return res.status(404).json({ message: `No dealerships found in state: ${state}` });
    }
    res.status(200).json(dealerships);
  } catch (error) {
    res.status(500).json({ error: `Error fetching dealerships for state: ${state}` });
  }
});

app.get('/fetchDealer/:id', async (req, res) => {
  try {
    const dealershipId = parseInt(req.params.id, 10);
    if (isNaN(dealershipId)) {
      return res.status(400).json({ error: 'Invalid dealership ID format' });
    }
    const dealership = await Dealerships.findOne({ id: dealershipId });
    if (!dealership) {
      return res.status(404).json({ message: 'Dealer not found' });
    }
    res.status(200).json(dealership);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealership by ID' });
  }
});

app.post('/insert_review', async (req, res) => {
  try {
    const data = req.body;
    const documents = await Reviews.find().sort({ id: -1 });
    const newId = (documents[0] && documents[0].id ? documents[0].id : 0) + 1;

    const review = new Reviews({
      id: newId,
      name: data.name,
      dealership: data.dealership,
      review: data.review,
      purchase: data.purchase,
      purchase_date: data.purchase_date,
      car_make: data.car_make,
      car_model: data.car_model,
      car_year: data.car_year,
    });

    const savedReview = await review.save();
    res.json(savedReview);
  } catch (error) {
    res.status(500).json({ error: 'Error inserting review' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
