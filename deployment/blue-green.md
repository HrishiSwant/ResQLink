# ResQLink Blue-Green Deployment

## Concept

Blue-Green Deployment uses two separate application environments:

- Blue = Current production version
- Green = New version being prepared

Only one environment receives production traffic at a time.

## ResQLink Flow

```text
                 Production Traffic
                        |
                        v
                 +-------------+
                 | Load Balancer|
                 +-------------+
                        |
                +-------+-------+
                |               |
                v               v
             BLUE            GREEN
          Current Version   New Version
             Active           Testing
