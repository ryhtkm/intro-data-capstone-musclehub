{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Capstone Project 1: MuscleHub AB Test"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: Get started with SQL"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Like most businesses, Janet keeps her data in a SQL database.  Normally, you'd download the data from her database to a csv file, and then load it into a Jupyter Notebook using Pandas.\n",
    "\n",
    "For this project, you'll have to access SQL in a slightly different way.  You'll be using a special Codecademy library that lets you type SQL queries directly into this Jupyter notebook.  You'll have pass each SQL query as an argument to a function called `sql_query`.  Each query will return a Pandas DataFrame.  Here's an example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# This import only needs to happen once, at the beginning of the notebook\n",
    "from codecademySQL import sql_query"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>visit_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Karen</td>\n",
       "      <td>Manning</td>\n",
       "      <td>Karen.Manning@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Annette</td>\n",
       "      <td>Boone</td>\n",
       "      <td>AB9982@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Salvador</td>\n",
       "      <td>Merritt</td>\n",
       "      <td>SalvadorMerritt12@outlook.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Martha</td>\n",
       "      <td>Maxwell</td>\n",
       "      <td>Martha.Maxwell@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Andre</td>\n",
       "      <td>Mayer</td>\n",
       "      <td>AndreMayer90@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                          email  gender  \\\n",
       "0      0      Karen   Manning        Karen.Manning@gmail.com  female   \n",
       "1      1    Annette     Boone               AB9982@gmail.com  female   \n",
       "2      2   Salvador   Merritt  SalvadorMerritt12@outlook.com    male   \n",
       "3      3     Martha   Maxwell       Martha.Maxwell@gmail.com  female   \n",
       "4      4      Andre     Mayer         AndreMayer90@gmail.com    male   \n",
       "\n",
       "  visit_date  \n",
       "0     5-1-17  \n",
       "1     5-1-17  \n",
       "2     5-1-17  \n",
       "3     5-1-17  \n",
       "4     5-1-17  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Here's an example of a query that just displays some data\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM visits\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Here's an example where we save the data to a DataFrame\n",
    "df2 = sql_query('''\n",
    "SELECT *\n",
    "FROM applications\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: Get your dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's get started!\n",
    "\n",
    "Janet of MuscleHub has a SQLite database, which contains several tables that will be helpful to you in this investigation:\n",
    "- `visits` contains information about potential gym customers who have visited MuscleHub\n",
    "- `fitness_tests` contains information about potential customers in \"Group A\", who were given a fitness test\n",
    "- `applications` contains information about any potential customers (both \"Group A\" and \"Group B\") who filled out an application.  Not everyone in `visits` will have filled out an application.\n",
    "- `purchases` contains information about customers who purchased a membership to MuscleHub.\n",
    "\n",
    "Use the space below to examine each table."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   index first_name last_name                          email  gender  \\\n",
      "0      0      Karen   Manning        Karen.Manning@gmail.com  female   \n",
      "1      1    Annette     Boone               AB9982@gmail.com  female   \n",
      "2      2   Salvador   Merritt  SalvadorMerritt12@outlook.com    male   \n",
      "3      3     Martha   Maxwell       Martha.Maxwell@gmail.com  female   \n",
      "4      4      Andre     Mayer         AndreMayer90@gmail.com    male   \n",
      "\n",
      "  visit_date  \n",
      "0     5-1-17  \n",
      "1     5-1-17  \n",
      "2     5-1-17  \n",
      "3     5-1-17  \n",
      "4     5-1-17  \n",
      "   index first_name last_name                      email  gender visit_date\n",
      "0   5945    Armando   Mccarty  Armando.Mccarty@gmail.com    male     9-9-17\n",
      "1   5946     Sidney     Noble       SNoble1971@gmail.com    male     9-9-17\n",
      "2   5947     Walter    Lowery    WalterLowery8@gmail.com    male     9-9-17\n",
      "3   5948      Kathy    Macias      KMacias1975@gmail.com  female     9-9-17\n",
      "4   5949     Glenda   Mullins           GM2973@gmail.com  female     9-9-17\n"
     ]
    }
   ],
   "source": [
    "# Examine visits here\n",
    "visits = sql_query('''\n",
    "SELECT *\n",
    "FROM visits\n",
    "LIMIT 5\n",
    "''')\n",
    "print visits\n",
    "\n",
    "latest_visit = sql_query('''\n",
    "SELECT *\n",
    "FROM visits\n",
    "ORDER BY visit_date DESC\n",
    "LIMIT 5\n",
    "''')\n",
    "print latest_visit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   index first_name last_name                   email  gender  \\\n",
      "0      0        Kim    Walter   KimWalter58@gmail.com  female   \n",
      "1      1        Tom   Webster        TW3857@gmail.com    male   \n",
      "2      2     Marcus     Bauer  Marcus.Bauer@gmail.com    male   \n",
      "3      3    Roberta      Best      RB6305@hotmail.com  female   \n",
      "4      4     Carrie   Francis      CF1896@hotmail.com  female   \n",
      "\n",
      "  fitness_test_date  \n",
      "0        2017-07-03  \n",
      "1        2017-07-02  \n",
      "2        2017-07-01  \n",
      "3        2017-07-02  \n",
      "4        2017-07-05  \n"
     ]
    }
   ],
   "source": [
    "# Examine fitness_tests here\n",
    "fitness_tests = sql_query('''\n",
    "SELECT *\n",
    "FROM fitness_tests\n",
    "LIMIT 5\n",
    "''')\n",
    "print fitness_tests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   index first_name last_name                    email  gender  \\\n",
      "0      0        Roy    Abbott    RoyAbbott32@gmail.com    male   \n",
      "1      1      Agnes   Acevedo  AgnesAcevedo1@gmail.com  female   \n",
      "2      2    Roberta   Acevedo         RA8063@gmail.com  female   \n",
      "3      3     Darren    Acosta  DAcosta1996@hotmail.com    male   \n",
      "4      4     Vernon    Acosta    VAcosta1975@gmail.com    male   \n",
      "\n",
      "  application_date  \n",
      "0       2017-08-12  \n",
      "1       2017-09-29  \n",
      "2       2017-09-15  \n",
      "3       2017-07-26  \n",
      "4       2017-07-14  \n"
     ]
    }
   ],
   "source": [
    "# Examine applications here\n",
    "applications = sql_query('''\n",
    "SELECT *\n",
    "FROM applications\n",
    "LIMIT 5\n",
    "''')\n",
    "print applications"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   index first_name last_name                    email  gender purchase_date\n",
      "0      0        Roy    Abbott    RoyAbbott32@gmail.com    male    2017-08-18\n",
      "1      1    Roberta   Acevedo         RA8063@gmail.com  female    2017-09-16\n",
      "2      2     Vernon    Acosta    VAcosta1975@gmail.com    male    2017-07-20\n",
      "3      3     Darren    Acosta  DAcosta1996@hotmail.com    male    2017-07-27\n",
      "4      4       Dawn    Adkins    Dawn.Adkins@gmail.com  female    2017-08-24\n"
     ]
    }
   ],
   "source": [
    "# Examine purchases here\n",
    "purchases = sql_query('''\n",
    "SELECT *\n",
    "FROM purchases\n",
    "LIMIT 5\n",
    "''')\n",
    "print purchases"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'd like to download a giant DataFrame containing all of this data.  You'll need to write a query that does the following things:\n",
    "\n",
    "1. Not all visits in  `visits` occurred during the A/B test.  You'll only want to pull data where `visit_date` is on or after `7-1-17`.\n",
    "\n",
    "2. You'll want to perform a series of `LEFT JOIN` commands to combine the four tables that we care about.  You'll need to perform the joins on `first_name`, `last_name`, and `email`.  Pull the following columns:\n",
    "\n",
    "\n",
    "- `visits.first_name`\n",
    "- `visits.last_name`\n",
    "- `visits.gender`\n",
    "- `visits.email`\n",
    "- `visits.visit_date`\n",
    "- `fitness_tests.fitness_test_date`\n",
    "- `applications.application_date`\n",
    "- `purchases.purchase_date`\n",
    "\n",
    "Save the result of this query to a variable called `df`.\n",
    "\n",
    "Hint: your result should have 5004 rows.  Does it?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5004\n",
      "  first_name last_name  gender                   email visit_date  \\\n",
      "0        Kim    Walter  female   KimWalter58@gmail.com     7-1-17   \n",
      "1        Tom   Webster    male        TW3857@gmail.com     7-1-17   \n",
      "2     Edward     Bowen    male  Edward.Bowen@gmail.com     7-1-17   \n",
      "3     Marcus     Bauer    male  Marcus.Bauer@gmail.com     7-1-17   \n",
      "4    Roberta      Best  female      RB6305@hotmail.com     7-1-17   \n",
      "\n",
      "  fitness_test_date application_date purchase_date  \n",
      "0        2017-07-03             None          None  \n",
      "1        2017-07-02             None          None  \n",
      "2              None       2017-07-04    2017-07-04  \n",
      "3        2017-07-01       2017-07-03    2017-07-05  \n",
      "4        2017-07-02             None          None  \n"
     ]
    }
   ],
   "source": [
    "df = sql_query('''\n",
    "SELECT v.first_name,\n",
    "    v.last_name,\n",
    "    v.gender,\n",
    "    v.email,\n",
    "    v.visit_date,\n",
    "    f.fitness_test_date,\n",
    "    ap.application_date,\n",
    "    p.purchase_date\n",
    "FROM visits as v\n",
    "LEFT JOIN fitness_tests as f\n",
    "       ON v.first_name = f.first_name\n",
    "       AND v.last_name = f.last_name\n",
    "       AND v.email = f.email\n",
    "LEFT JOIN applications as ap\n",
    "       ON v.first_name = ap.first_name\n",
    "       AND v.last_name = ap.last_name\n",
    "       AND v.email = ap.email\n",
    "LEFT JOIN purchases as p\n",
    "       ON v.first_name = p.first_name\n",
    "       AND v.last_name = p.last_name\n",
    "       AND v.email = p.email\n",
    "WHERE v.visit_date >= '7-1-17'\n",
    "''')\n",
    "print len(df)\n",
    "print df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3: Investigate the A and B groups"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We have some data to work with! Import the following modules so that we can start doing analysis:\n",
    "- `import pandas as pd`\n",
    "- `from matplotlib import pyplot as plt`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We're going to add some columns to `df` to help us with our analysis.\n",
    "\n",
    "Start by adding a column called `ab_test_group`.  It should be `A` if `fitness_test_date` is not `None`, and `B` if `fitness_test_date` is `None`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  first_name last_name  gender                   email visit_date  \\\n",
      "0        Kim    Walter  female   KimWalter58@gmail.com     7-1-17   \n",
      "1        Tom   Webster    male        TW3857@gmail.com     7-1-17   \n",
      "2     Edward     Bowen    male  Edward.Bowen@gmail.com     7-1-17   \n",
      "3     Marcus     Bauer    male  Marcus.Bauer@gmail.com     7-1-17   \n",
      "4    Roberta      Best  female      RB6305@hotmail.com     7-1-17   \n",
      "\n",
      "  fitness_test_date application_date purchase_date ab_test_group  \n",
      "0        2017-07-03             None          None             A  \n",
      "1        2017-07-02             None          None             A  \n",
      "2              None       2017-07-04    2017-07-04             B  \n",
      "3        2017-07-01       2017-07-03    2017-07-05             A  \n",
      "4        2017-07-02             None          None             A  \n"
     ]
    }
   ],
   "source": [
    "df[\"ab_test_group\"] = df.fitness_test_date.apply(lambda x: \"B\" if x == None else \"A\")\n",
    "print df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's do a quick sanity check that Janet split her visitors such that about half are in A and half are in B.\n",
    "\n",
    "Start by using `groupby` to count how many users are in each `ab_test_group`.  Save the results to `ab_counts`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ab_test_group\n",
      "A    2504\n",
      "B    2500\n",
      "Name: first_name, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "ab_counts = df.groupby(\"ab_test_group\").first_name.count().reindex()\n",
    "print ab_counts"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'll want to include this information in our presentation.  Let's create a pie cart using `plt.pie`.  Make sure to include:\n",
    "- Use `plt.axis('equal')` so that your pie chart looks nice\n",
    "- Add a legend labeling `A` and `B`\n",
    "- Use `autopct` to label the percentage of each group\n",
    "- Save your figure as `ab_test_pie_chart.png`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.pie(ab_counts,\n",
    "       labels=[\"A\",\"B\"],\n",
    "       autopct=\"%0.2f%%\")\n",
    "plt.axis(\"equal\")\n",
    "plt.savefig(\"ab_test_pie_chart.png\")\n",
    "plt.show()\n",
    "plt.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Who picks up an application?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Recall that the sign-up process for MuscleHub has several steps:\n",
    "1. Take a fitness test with a personal trainer (only Group A)\n",
    "2. Fill out an application for the gym\n",
    "3. Send in their payment for their first month's membership\n",
    "\n",
    "Let's examine how many people make it to Step 2, filling out an application.\n",
    "\n",
    "Start by creating a new column in `df` called `is_application` which is `Application` if `application_date` is not `None` and `No Application`, otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  first_name last_name  gender                   email visit_date  \\\n",
      "0        Kim    Walter  female   KimWalter58@gmail.com     7-1-17   \n",
      "1        Tom   Webster    male        TW3857@gmail.com     7-1-17   \n",
      "2     Edward     Bowen    male  Edward.Bowen@gmail.com     7-1-17   \n",
      "3     Marcus     Bauer    male  Marcus.Bauer@gmail.com     7-1-17   \n",
      "4    Roberta      Best  female      RB6305@hotmail.com     7-1-17   \n",
      "\n",
      "  fitness_test_date application_date purchase_date ab_test_group  \\\n",
      "0        2017-07-03             None          None             A   \n",
      "1        2017-07-02             None          None             A   \n",
      "2              None       2017-07-04    2017-07-04             B   \n",
      "3        2017-07-01       2017-07-03    2017-07-05             A   \n",
      "4        2017-07-02             None          None             A   \n",
      "\n",
      "   is_application  \n",
      "0  No Application  \n",
      "1  No Application  \n",
      "2     Application  \n",
      "3     Application  \n",
      "4  No Application  \n"
     ]
    }
   ],
   "source": [
    "df[\"is_application\"]= df.application_date.apply(lambda x: \"No Application\" if x == None else \"Application\")\n",
    "print df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, using `groupby`, count how many people from Group A and Group B either do or don't pick up an application.  You'll want to group by `ab_test_group` and `is_application`.  Save this new DataFrame as `app_counts`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  ab_test_group  is_application  first_name\n",
      "0             A     Application         250\n",
      "1             A  No Application        2254\n",
      "2             B     Application         325\n",
      "3             B  No Application        2175\n"
     ]
    }
   ],
   "source": [
    "app_counts = df.groupby([\"ab_test_group\",\"is_application\"]).first_name.count().reset_index()\n",
    "print app_counts"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We're going to want to calculate the percent of people in each group who complete an application.  It's going to be much easier to do this if we pivot `app_counts` such that:\n",
    "- The `index` is `ab_test_group`\n",
    "- The `columns` are `is_application`\n",
    "Perform this pivot and save it to the variable `app_pivot`.  Remember to call `reset_index()` at the end of the pivot!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_application ab_test_group  Application  No Application\n",
      "0                          A          250            2254\n",
      "1                          B          325            2175\n"
     ]
    }
   ],
   "source": [
    "app_pivot = app_counts.pivot(columns = \"is_application\",index=\"ab_test_group\",values=\"first_name\").reset_index()\n",
    "print app_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Define a new column called `Total`, which is the sum of `Application` and `No Application`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_application ab_test_group  Application  No Application  Total\n",
      "0                          A          250            2254   2504\n",
      "1                          B          325            2175   2500\n"
     ]
    }
   ],
   "source": [
    "total_row = lambda row:row.Application + row[\"No Application\"]\n",
    "app_pivot[\"Total\"]= app_pivot.apply(total_row,axis=1)\n",
    "print app_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculate another column called `Percent with Application`, which is equal to `Application` divided by `Total`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_application ab_test_group  Application  No Application  Total  Percent\n",
      "0                          A          250            2254   2504  0.09984\n",
      "1                          B          325            2175   2500  0.13000\n"
     ]
    }
   ],
   "source": [
    "percent_app = lambda row:1.0*row.Application/row.Total\n",
    "app_pivot[\"Percent\"] = app_pivot.apply(percent_app,axis=1)\n",
    "print app_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like more people from Group B turned in an application.  Why might that be?\n",
    "\n",
    "We need to know if this difference is statistically significant.\n",
    "\n",
    "Choose a hypothesis tests, import it from `scipy` and perform it.  Be sure to note the p-value.\n",
    "Is this result significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.000964782760072\n"
     ]
    }
   ],
   "source": [
    "from scipy.stats import chi2_contingency as chi2\n",
    "contingency_table = [[250,2254],[325,2175]]\n",
    "_,p_value,_,_= chi2(contingency_table)\n",
    "print p_value"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Who purchases a membership?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Of those who picked up an application, how many purchased a membership?\n",
    "\n",
    "Let's begin by adding a column to `df` called `is_member` which is `Member` if `purchase_date` is not `None`, and `Not Member` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  first_name last_name  gender                   email visit_date  \\\n",
      "0        Kim    Walter  female   KimWalter58@gmail.com     7-1-17   \n",
      "1        Tom   Webster    male        TW3857@gmail.com     7-1-17   \n",
      "2     Edward     Bowen    male  Edward.Bowen@gmail.com     7-1-17   \n",
      "3     Marcus     Bauer    male  Marcus.Bauer@gmail.com     7-1-17   \n",
      "4    Roberta      Best  female      RB6305@hotmail.com     7-1-17   \n",
      "\n",
      "  fitness_test_date application_date purchase_date ab_test_group  \\\n",
      "0        2017-07-03             None          None             A   \n",
      "1        2017-07-02             None          None             A   \n",
      "2              None       2017-07-04    2017-07-04             B   \n",
      "3        2017-07-01       2017-07-03    2017-07-05             A   \n",
      "4        2017-07-02             None          None             A   \n",
      "\n",
      "   is_application   is_member  \n",
      "0  No Application  Not Member  \n",
      "1  No Application  Not Member  \n",
      "2     Application      Member  \n",
      "3     Application      Member  \n",
      "4  No Application  Not Member  \n"
     ]
    }
   ],
   "source": [
    "df[\"is_member\"] = df.purchase_date.apply(lambda x: \"Not Member\" if x == None else \"Member\")\n",
    "print df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, let's create a DataFrame called `just_apps` the contains only people who picked up an application."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   first_name last_name  gender                    email visit_date  \\\n",
      "2      Edward     Bowen    male   Edward.Bowen@gmail.com     7-1-17   \n",
      "3      Marcus     Bauer    male   Marcus.Bauer@gmail.com     7-1-17   \n",
      "9    Salvador  Cardenas    male  SCardenas1980@gmail.com     7-1-17   \n",
      "11    Valerie     Munoz  female     VMunoz1998@gmail.com     7-1-17   \n",
      "35    Michael     Burks    male         MB9820@gmail.com     7-1-17   \n",
      "\n",
      "   fitness_test_date application_date purchase_date ab_test_group  \\\n",
      "2               None       2017-07-04    2017-07-04             B   \n",
      "3         2017-07-01       2017-07-03    2017-07-05             A   \n",
      "9         2017-07-07       2017-07-06          None             A   \n",
      "11        2017-07-03       2017-07-05    2017-07-06             A   \n",
      "35              None       2017-07-07    2017-07-13             B   \n",
      "\n",
      "   is_application   is_member  \n",
      "2     Application      Member  \n",
      "3     Application      Member  \n",
      "9     Application  Not Member  \n",
      "11    Application      Member  \n",
      "35    Application      Member  \n"
     ]
    }
   ],
   "source": [
    "just_apps = df[df.is_application == \"Application\"]\n",
    "print just_apps.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Now, let's do a `groupby` to find out how many people in `just_apps` are and aren't members from each group.  Follow the same process that we did in Step 4, including pivoting the data.  You should end up with a DataFrame that looks like this:\n",
    "\n",
    "|is_member|ab_test_group|Member|Not Member|Total|Percent Purchase|\n",
    "|-|-|-|-|-|-|\n",
    "|0|A|?|?|?|?|\n",
    "|1|B|?|?|?|?|\n",
    "\n",
    "Save your final DataFrame as `member_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    is_member ab_test_group  first_name\n",
      "0      Member             A         200\n",
      "1      Member             B         250\n",
      "2  Not Member             A          50\n",
      "3  Not Member             B          75\n",
      "is_member ab_test_group  Member  Not Member  Total   Percent\n",
      "0                     A     200          50    250  0.800000\n",
      "1                     B     250          75    325  0.769231\n"
     ]
    }
   ],
   "source": [
    "members_counts = just_apps.groupby([\"is_member\",\"ab_test_group\"]).first_name.count().reset_index()\n",
    "print members_counts\n",
    "members_pivot = members_counts.pivot(columns =\"is_member\",index=\"ab_test_group\",values=\"first_name\").reset_index()\n",
    "members_pivot[\"Total\"] = members_pivot.apply(lambda row:row[\"Member\"] + row[\"Not Member\"],axis=1)\n",
    "members_pivot[\"Percent\"] = members_pivot.apply(lambda row: 1.0* row[\"Member\"]/row[\"Total\"],axis=1)\n",
    "print members_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like people who took the fitness test were more likely to purchase a membership **if** they picked up an application.  Why might that be?\n",
    "\n",
    "Just like before, we need to know if this difference is statistically significant.  Choose a hypothesis tests, import it from `scipy` and perform it.  Be sure to note the p-value.\n",
    "Is this result significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.432586460511\n"
     ]
    }
   ],
   "source": [
    "from scipy.stats import chi2_contingency as chi2\n",
    "contingency_table = [[200,50],[250,75]]\n",
    "_,p_value,_,_= chi2(contingency_table)\n",
    "print p_value"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Previously, we looked at what percent of people **who picked up applications** purchased memberships.  What we really care about is what percentage of **all visitors** purchased memberships.  Return to `df` and do a `groupby` to find out how many people in `df` are and aren't members from each group.  Follow the same process that we did in Step 4, including pivoting the data.  You should end up with a DataFrame that looks like this:\n",
    "\n",
    "|is_member|ab_test_group|Member|Not Member|Total|Percent Purchase|\n",
    "|-|-|-|-|-|-|\n",
    "|0|A|?|?|?|?|\n",
    "|1|B|?|?|?|?|\n",
    "\n",
    "Save your final DataFrame as `final_member_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    is_member ab_test_group  first_name\n",
      "0      Member             A         200\n",
      "1      Member             B         250\n",
      "2  Not Member             A        2304\n",
      "3  Not Member             B        2250\n",
      "is_member ab_test_group  Member  Not Member  Total   Percent\n",
      "0                     A     200        2304   2504  0.079872\n",
      "1                     B     250        2250   2500  0.100000\n"
     ]
    }
   ],
   "source": [
    "all_visitors = df.groupby([\"is_member\",\"ab_test_group\"]).first_name.count().reset_index()\n",
    "print all_visitors\n",
    "final_member_pivot = all_visitors.pivot(columns =\"is_member\",index=\"ab_test_group\",values=\"first_name\").reset_index()\n",
    "final_member_pivot[\"Total\"] = final_member_pivot.apply(lambda row:row[\"Member\"] + row[\"Not Member\"],axis=1)\n",
    "final_member_pivot[\"Percent\"] = final_member_pivot.apply(lambda row: 1.0* row[\"Member\"]/row[\"Total\"],axis=1)\n",
    "print final_member_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Previously, when we only considered people who had **already picked up an application**, we saw that there was no significant difference in membership between Group A and Group B.\n",
    "\n",
    "Now, when we consider all people who **visit MuscleHub**, we see that there might be a significant different in memberships between Group A and Group B.  Perform a significance test and check."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.stats import chi2_contingency as chi2\n",
    "contingency_table = [[250,2304],[250,2250]]\n",
    "_,p_value,_,_= chi2(contingency_table)\n",
    "print p_value"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5: Summarize the acquisition funel with a chart"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'd like to make a bar chart for Janet that shows the difference between Group A (people who were given the fitness test) and Group B (people who were not given the fitness test) at each state of the process:\n",
    "- Percent of visitors who apply\n",
    "- Percent of applicants who purchase a membership\n",
    "- Percent of visitors who purchase a membership\n",
    "\n",
    "Create one plot for **each** of the three sets of percentages that you calculated in `app_pivot`, `member_pivot` and `final_member_pivot`.  Each plot should:\n",
    "- Label the two bars as `Fitness Test` and `No Fitness Test`\n",
    "- Make sure that the y-axis ticks are expressed as percents (i.e., `5%`)\n",
    "- Have a title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ax = plt.subplot()\n",
    "n = 1 #nth datesets \n",
    "t = 1 # number of sets of bar\n",
    "d = len(app_pivot)\n",
    "w = 0.8 #width\n",
    "store_x = [t*elements + w*n for elements in range(d)]\n",
    "plt.bar(store_x,\n",
    "       app_pivot['Percent'].values)\n",
    "ax.set_xticks(store_x)\n",
    "ax.set_xticklabels(['Fitness Test', 'No Fitness Test'])\n",
    "ax.set_yticks([0, 0.05, 0.10, 0.15, 0.20])\n",
    "ax.set_yticklabels(['0%', '5%', '10%', '15%', '20%'])\n",
    "plt.title(\"Percent of visitors who apply\")\n",
    "plt.show()\n",
    "plt.savefig('percent_visitors_apply.png')\n",
    "plt.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ax = plt.subplot()\n",
    "plt.bar(range(len(members_pivot)),\n",
    "       members_pivot['Percent'].values)\n",
    "ax.set_xticks(range(len(members_pivot)))\n",
    "ax.set_xticklabels(['Fitness Test', 'No Fitness Test'])\n",
    "ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])\n",
    "ax.set_yticklabels(['0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'])\n",
    "plt.title(\"Percent of applicants who purchase a membership\")\n",
    "plt.show()\n",
    "plt.savefig('percent_memberonly_apply.png')\n",
    "plt.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ax = plt.subplot()\n",
    "plt.bar(range(len(final_member_pivot)),\n",
    "       final_member_pivot['Percent'].values)\n",
    "ax.set_xticks(range(len(final_member_pivot)))\n",
    "ax.set_xticklabels(['Fitness Test', 'No Fitness Test'])\n",
    "ax.set_yticks([0, 0.05, 0.10, 0.15, 0.20])\n",
    "ax.set_yticklabels(['0%', '5%', '10%', '15%', '20%'])\n",
    "plt.title(\"Percent of visitors who purchase a membership\")\n",
    "plt.show()\n",
    "plt.savefig('percent_final_apply.png')\n",
    "plt.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
