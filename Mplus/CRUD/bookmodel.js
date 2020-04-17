const mongoose = require("mongoose");

const bookSchema = mongoose.Schema({
  title: {
    type: String,
  },
  author: {
    type: String,
  },
  date: {
    type: Date,
  },
  pages: {
    type: Number,
  },
  genre: {
    type: String,
  },
});

module.exports = mongoose.model("Book", bookSchema);
