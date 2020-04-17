var express = require("express"),
  path = require("path"),
  bodyParser = require("body-parser"),
  cors = require("cors"),
  mongoose = require("mongoose");

mongoose.connect("mongodb://localhost:27017/vuecrud").then(
  () => {
    console.log("Database connected");
  },
  (err) => {
    console.log("Error connect to database" + err);
  }
);

var router = express.Router();
var bookrouter = require("./bookcontroller.js");
const app = express();
app.use(express.static("public"));
app.use(bodyParser.json());
app.use(cors());
app.listen(8081, () => {
  console.log("Server started on port 8081");
});

app.use("/books", bookrouter);

router.get("/", (req, res) => {
  res.render("index");
});
