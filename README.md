# Sales CRM

A simple CRM to manage sales, inventory and customers. Dashboard for various analytics of the business financials and to spot trends in product sales and demands. Option to integrate with other services via the REST API.

I also plan to utilize pytorch to offer some fancy prediction/trends analysis.

## Stack

Frontend: TBC..

Backend: Python, FastAPI, Prisma and Postgres

## TODO

Client:

> Haven't planned this out yet.

Server:

-   [x] Create schema for database.
-   [x] Create endpoints to CRUD Customer
-   [x] Create endpoint to get all Customers.
-   [ ] Create endpoints to CRUD CustomerContact
-   [ ] Create endpoints to CRD CustomerReferral

## Setup

### Server

1. Install requirements, within the `server/` folder run:

    > `pip install -r requirements.txt`

2. Modify the `.env` with your `DATABASE_URL`. An example is shown below:

    > `DATABASE_URL="postgresql://username:password@localhost:32768/postgres?schema=sales-crm"`

3. Push the schema to the db:

    > `prisma db push`

4. To start the server run:
    > `uvicorn main:fast_api --reload`

### Client

_work in progress_
