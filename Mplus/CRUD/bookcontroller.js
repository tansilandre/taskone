var Book = require('./bookmodel.js');
var express = require('express');
var router = express.Router();

module.exports = router;


router.route('/create').post((req, res) => {
  var book = new Book({
    title : req.body.title,
    author : req.body.author,
    date : req.body.date,
    pages : req.body.pages,
    genre : req.body.genre
  });
   book.save().then( book => {
   res.status(200).json({'message': 'Book successfully added '});
   })
   .catch(err => {
    res.status(400).send("Error when saving to database");
   });
});

router.route('/books').get((req, res) => {
  Book.find((err, books) =>{
    if(err){
      console.log(err);
    }
    else {
      res.json(books);
    }
  });
});

router.route('/books/:id').get((req, res) => {
  var id = req.params.id;
  Book.findById(id, (err, book) =>{
      res.json(book);
  });
});

router.route('/books/:id').put((req, res) => {
  Book.findById(req.params.id, (err, book) => {
    if (!book)
      return next(new Error('Error getting the book!'));
    else {
      book.title = req.body.title;
      book.save().then( book => {
          res.json('Book updated successfully');
      })
      .catch(err => {
            res.status(400).send("Error when updating the book");
      });
    }
  });
});

router.route('/books/:id/delete').get((req, res) => {
  Book.findByIdAndRemove({_id: req.params.id}, (err,book) =>{
        if(err) res.json(err);
        else res.json('Book successfully removed');
    });
});
