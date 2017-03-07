Midterm Exam - Spring 2017

Dependency and Installation from sources:
Python 3.5.2
NY Times Article
pip install nytimesarticle
Matplotlib
pip install matplotlib
Store API key as environment variable



Question 1 :
Exploratory Data Analysis of Enron Emails

Dataset : CMU ENRON Dataset
1.82 GB of email data from all the employees of ENRON starting from December 1999 to November 2001. This dataset contains data from about 150 users, mostly senior management of Enron, organized into folders. The corpus contains a total of about 0.5 million messages. The dataset consists of 517,431 messages that belong to 150 users, mostly senior management of the Enron Corp. Although the dataset is huge, folders of particular users are often quite sparse.

Analysis and Information:
From the outputs seen above we can understand number of meeting related emails, casual emails, process related emails and core business related emails and when they were sent. I wanted to plot the probability distribution of each type of email over time, but because of time constraint just creating outputs in csv. From the output we can analyze that most of the enrol emails consisted of Business Process. Casual meeting related emails were more than official meeting, which can be a result of fraudulent activities carried on within Enron. There were moderate number of core business related emails sent. If we observe carefully there is a huge spike in core business emails towards the end, maybe to hide their fraudulent activities. Also we have analyzed top 10 emails whom Jeffrey Skilling, the CEO of Enron, who was involved in the scandal interacted with. Further investigation can be carried out on these emails.

References:
https://www.stat.berkeley.edu/~aldous/Research/Ugrad/HarishKumarReport.pdf
http://www.investopedia.com/updates/enron-scandal-summary/



Question 2 Part 1:
NYT API data analysis using article api.

Dataset:
Article Search dataset for Obama and Trump gathered using api-key. I have collected about 120 json files related to both Obama and Trump, each consisting about 10 articles. So basically 2400 articles were used in all for analyzing the data.

Analysis and Information:
Thus we can conclude that NYTimes.com do publish articles which are more neutral in case of Obama. Also we can see that NYTimes.com do publish a lot of negative articles in case of Trump. From the graph we can also analyze, in case of positive articles, when 240 positive articles about Trump were published, 274 positive articles about Obama were published.
While in case of negative articles when 277 negative articles regarding Obama, a considerable amount of 397 negative articles were published about Trump.
Thus, we can conclude that most of the authors of NYTimes.com of the articles write in favor of Obama.



Question 2 Part 2:
NYT API data analysis using community api.

Dataset 1:
Community dataset regarding Presidential Election using community api-key. Data was collected for the month of November from 11/10/2016 to 11/30/2016. For this question, I am trying to analyze sentiments of users after the results of Presidential Election were declared on 9th of November, 2016.

Analysis and Information:
Thus we can conclude that users choose to stay neutral on this topic. Though number of negative comments on this topic is slightly more than positive comments but still we can't infer much considering the small amount of data. We might come to a better conclusion if there is no data constraints.
Also we can conclude that the number of users on NYTimes.com, not happy with the result of the presidential election are more. As we can see the number of negative comments is more than the number of positive comments. The output of the analysis and comments after sorting have been stored in the csv file.
