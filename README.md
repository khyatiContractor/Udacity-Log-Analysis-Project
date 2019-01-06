In this project, you will stretch your SQL database skills. You will get practice interacting with a live database both from the command line and from your code. You will explore a large database with over a million rows. And you will build and refine complex queries and use them to draw business conclusions from data.

# Report generation
Building an informative summary from logs is a real task that comes up very often in software engineering. For instance, at Udacity we collect logs to help us measure student progress and the success of our courses. The reporting tools we use to analyze those logs involve hundreds of lines of SQL.

# The virtual machine
This project makes use of the same Linux-based virtual machine (VM) as the preceding lessons.

If you skipped those lessons and came right to this project, that's OK! However, you will need to go back to the instructions to install the virtual machine. Please see previous lessons to complete the installation process.

This will give you the PostgreSQL database and support software needed for this project. If you have used an older version of this VM, you may need to install it into a new directory.

If you need to bring the virtual machine back online:

    vagrant up
Then log into it with 

    vagrant ssh

# Download the data
To load the data, cd into the vagrant directory and use the command 

    psql -d news -f newsdata.sql

The database includes three tables:

The authors table -- includes information about the authors of articles.
The articles table -- includes the articles themselves.
The log table -- includes one entry for each time a user has accessed the site.

# Create View:

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
