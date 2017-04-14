PImage worldMapImage;
MercatorMap mercatorMap;

PVector berlin;
PVector sydney;
PVector sanFrancisco;

void setup() {
  size(400, 310);
  smooth();
  worldMapImage = loadImage("400px-Mercator-projection.jpg");
  mercatorMap = new MercatorMap(400, 310);
  berlin = mercatorMap.getScreenLocation(new PVector(52, 13));
  sydney = mercatorMap.getScreenLocation(new PVector(-33.86, 151.21));
  sanFrancisco = mercatorMap.getScreenLocation(new PVector(37.8, -122.4));
}

void draw() {
  image(worldMapImage, 0, 0, width, height);

  noStroke();
  fill(255, 0, 0, 200);
  
  ellipse(berlin.x, berlin.y, 6, 6);
  ellipse(sydney.x, sydney.y, 6, 6);
  ellipse(sanFrancisco.x, sanFrancisco.y, 6, 6);
}


