# Python OpenTelemetry Example

This repository contains a simple Python Flask application that demonstrates how to integrate OpenTelemetry for tracing and logging. The application generates logs and traces, and exports them to an OpenTelemetry Collector, which forwards them to Loki and Tempo for visualization and analysis.

## Overview

The application is a basic Flask web server with two endpoints:
- `/`: Returns a "Hello, world!" message and logs the request.
- `/health`: Returns an "OK" message and logs a health check message.

The application uses OpenTelemetry to instrument and export traces and logs.

## Features

- Traces HTTP requests and logs messages using OpenTelemetry.
- Exports traces and logs to an OpenTelemetry Collector.
- Forwards data from the OpenTelemetry Collector to Loki and Tempo.

## Getting Started

### Prerequisites

- Docker
- Docker Compose