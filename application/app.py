from flask import Flask
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
import logging

app = Flask(__name__)

# Tracer setup
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
span_processor = BatchSpanProcessor(OTLPSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

# Instrumentations
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
LoggingInstrumentor().instrument(set_logging_format=True)

# Logger setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)


@app.route('/')
def index():
    with tracer.start_as_current_span("index"):
        logger.info("Handling request on /")
        return "Hello, world!"


@app.route('/health')
def health():
    with tracer.start_as_current_span("health"):
        logger.info("Health Check")
        return "OK"
