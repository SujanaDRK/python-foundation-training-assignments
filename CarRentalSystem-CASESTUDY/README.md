# Car Rental System

A simple Python/MySQL backend to manage customers, vehicles, leases, and payments via a CLI.

## Brief 

1. **Database**  
   - Run `CarRentalSystem.sql` in MySQL to create tables and sample data.  
   - Edit `db.properties` with your MySQL credentials.

2. **Requirements**  
   ```bash
   pip install mysql-connector-python

3. **RunApp**
     python app/main.py
   
5. **RunApp**
     python -m unittest discover -s tests -p "test_*.py"

### Structure
CarRentalSystem-CASESTUDY/
├── app/                           # main.py CLI
├── dao/                           # database logic
├── entity/                        # data classes
├── exception/                     # custom errors
├── util/                          # db connection & config
├── tests/                         # unit tests
├── db.properties                  # DB settings
└── CarRentalSystem.sql            # schema & sample data


