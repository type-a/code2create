PImage worldMapImage;
MercatorMap mercatorMap;

PVector NY;
PVector HongKong;
PVector Bangalore;

void setup() 
{
  size(400,310);
  smooth();
  worldMapImage = loadImage("400px-Mercator-projection.jpg");
  mercatorMap = new MercatorMap(400, 310);
  NY = mercatorMap.getScreenLocation(new PVector(40.71,-74));
  HongKong = mercatorMap.getScreenLocation(new PVector(22.39,114.11));
  Bangalore = mercatorMap.getScreenLocation(new PVector(12.97,77.59));
}

void draw() 
{
  image(worldMapImage, 0, 0, width, height);

  noStroke();
  fill(255, 0, 0, 200);
  
  ellipse(NY.x, NY.y, 6, 6);
  ellipse(HongKong.x, HongKong.y, 6, 6);
  ellipse(Bangalore.x, Bangalore.y, 6, 6);
}

