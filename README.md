# **+EV Betting Model 📈**

## **Overview**
This is a personal project showcasing my **+EV betting model** that identifies and tracks NBA player prop bets. The model scrapes betting lines, calculates expected value (EV), and logs bets that meet the model criteria.

## **Live Site**
💻 [Visit the Live Site](https://d1nzshyp2a8e2d.cloudfront.net/)

## **Tech Stack**
- **Frontend:** React (Vite + TS)  
- **Backend:** AWS Lambda, API Gateway  
- **Infrastructure:** S3 (REST API), CloudFront (CDN), MongoDB Atlas (Data Storage)
![image](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)

## **How It Works**
1. **Bet Scraping**: The model pings an API every 5 minutes to check for betting lines with postive expected value.  
2. **Selection Criteria**: Bets are “placed” if they meet parameters defined by the model.  
3. **Storage & Grading**: The bets are logged and graded at the end of each day.  
4. **Frontend**: Users can select a date and view bets from that day or view profit over a period of time.

**Check out the "About" section of the website for more details.**

## **Usage**
To run locally:  
```sh
git clone https://github.com/ejjlittle/ev-betting-model.git  
cd frontend 
npm install  
npm run dev
```

Or just run the scraper to get live EV bets for placing:
```sh
git clone https://github.com/ejjlittle/ev-betting-model.git  
cd backend 
python -m placeBets.cnoScraper
```

## **Contact**
Ethan Little:
💼 [LinkedIn](https://www.linkedin.com/in/ethan-little-0587252a2/) | ✉️ elittle2@nd.edu