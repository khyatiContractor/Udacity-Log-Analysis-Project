# Log Analysis:
This project is part of Udacity FullStack Nano-Degree Program. 

## Report generation
In this project News database is used. Database can be accessed from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
Here SQL queries are written to analyze logs of news database. Those queries are as per below:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
    Output : 
    "Princess Shellfish Marries Prince Handsome" — 1201 views
    "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
    "Political Scandal Ends In Political Scandal" — 553 views
    
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
    Output:
    Ursula La Multa — 2304 views
    Rudolf von Treppenwitz — 1985 views
    Markoff Chaney — 1723 views
    Anonymous Contributor — 1023 views
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)
    Output:
    July 29, 2016 — 2.5% errors

## Database Overview
The database includes three tables:

        The authors table -- includes information about the authors of articles.

        The articles table -- includes the articles themselves.

        The log table -- includes one entry for each time a user has accessed the site.

### VirtualBox
VirtualBox is the software that actually runs the VM. You can download it from virtualbox.org. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.


### Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. You can download it from vagrantup.com. Install the version for your operating system.
 

Fetch the Source Code and VM Configuration

Fork the starter repo
Log into your personal Github account, and fork the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm).

Clone the remote to your local machine
From the terminal, run the following command (be sure to replace <username> with your GitHub username): git clone http://github.com/<username>/fullstack-nanodegree-vm fullstack

This will give you a directory named fullstack that is a clone of your remote fullstack-nanodegree-vm repository.

If you need to bring the virtual machine back online:
    cd /fullstack-nanodegree-vm/vagrant
    vagrant up
Then log into it with 
    vagrant ssh
    cd /vagrant/LogAnalsis

To load the data, cd into the vagrant directory and use the command 
    
    psql -d news -f newsdata.sql
    python news.db

Create View:
    psql news

    create view articalOrder as 
    select articles.slug as atitle, count(*) as numb 
    from log, articles 
    where articles.slug = substr(log.path, 10) 
    group by atitle 
    order by numb desc;

    create view errorData 
    as select time::timestamp::date as date, count(*) as errorcount  
    from log where status = '404 NOT FOUND' 
    group by date 
    order by errorcount desc;

    create view reqData 
    as select time::timestamp::date as date, count(*) as reqcount  
    from log group by date 
    order by reqcount desc;

    python forumdb.py
