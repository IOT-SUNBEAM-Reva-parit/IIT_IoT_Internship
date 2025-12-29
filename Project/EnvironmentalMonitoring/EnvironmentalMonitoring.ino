#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

// WiFi
const char* ssid     = "Reva";
const char* password = "reva292005";

// MQTT
const char* mqtt_server = "BEAGLEBONE_IP";

WiFiClient espClient;
PubSubClient client(espClient);

// DHT
#define DHTPIN 15
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// MQ‑2
#define MQ2PIN 34

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");

  client.setServer(mqtt_server, 1883);
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect("ESP32Sensor")) {
      Serial.println("Connected to MQTT");
    } else {
      delay(2000);
    }
  }
}

void loop() {
  if (!client.connected()) reconnect();
  client.loop();

  float temp = dht.readTemperature();
  float hum  = dht.readHumidity();
  int gasVal = analogRead(MQ2PIN);

  if (isnan(temp) || isnan(hum)) return;

  String payload = "{\"temp\":" + String(temp) +
                   ",\"hum\":" + String(hum) +
                   ",\"gas\":" + String(gasVal) + "}";

  client.publish("env/data", payload.c_str());
  delay(5000);
}