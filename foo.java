// camel-k: language=java

import org.apache.camel.builder.RouteBuilder;

public class foo extends RouteBuilder {

    @Override
    public void configure() throws Exception {

        from("vertx-websocket:192.168.1.28:443?consumeAsClient=true")
        // .unmarshal().json()
        // .setHeader("foo", jsonpath("$.r"))
        // .marshal().json()
        // .toD("paho-mqtt5:lulz/${header.foo}?brokerUrl=tcp://localhost:1883");
        .to("paho-mqtt5:deconz?brokerUrl=tcp://localhost:1883");

    }
}
