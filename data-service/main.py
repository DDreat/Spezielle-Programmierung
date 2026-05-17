from fastapi import FastAPI
import csv

app = FastAPI()


def load_metrics():
    columns = {}

    with open('../data/Interest.csv', newline='', encoding='utf-8') as file:

        reader = csv.reader(file)

        headers = next(reader)

        terms = headers[1:]

        for term in terms:
            columns[term] = []

        for row in reader:

            if not row:
                continue

            for index, term in enumerate(terms, start=1):

                value = row[index]

                if value == "<1":
                    value = 0

                if value == "":
                    continue

                columns[term].append(int(value))

        results = []

        for term, values in columns.items():
            
            if not values:
                continue

            mean = sum(values) / len(values)
            peak = max(values)

            first = values[0]
            last = values[-1]

            if last > first:
                trend = "increasing"
            elif last < first:
                trend = "decreasing"
            else:
                trend = "stable"

            results.append({
                "name": term,
                "mean": round(mean, 1),
                "peak": peak,
                "trend": trend
            })

    return {
        "terms": results
    }

@app.get("/metrics")
def get_metrics():
    return load_metrics()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/live")
def live():
    return {"status": "alive"}


@app.get("/ready")
def ready():
    return {"status": "ready"}