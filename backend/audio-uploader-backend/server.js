const express = require("express");
const { connect, Schema, model } = require("mongoose");
const multer = require("multer");
const path = require("path");

const app = express();
const PORT = 5000;

// Connect to MongoDB
connect("mongodb://127.0.0.1:27017/audio-uploader", {});

// Create a schema for storing audio files
const audioSchema = new Schema({
  originalname: String,
  filename: String,
});
const Audio = model("Audio", audioSchema);

// Set up Multer for file uploads
const storage = multer.diskStorage({
  destination: "uploads/",
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  },
});
const upload = multer({ storage });

// Upload route
app.post("/upload", upload.single("audio"), async (req, res) => {
  const { originalname, filename } = req.file;
  const newAudio = new Audio({ originalname, filename });
  await newAudio.save();
  res.send("File uploaded to MongoDB");
});

// Get all files route
app.get("/files", async (req, res) => {
  const files = await Audio.find();
  res.json(files);
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
