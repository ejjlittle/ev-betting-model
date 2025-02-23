# **+EV Betting Model**

## **Overview**
This is a personal project showcasing my **+EV betting model** that identifies and tracks NBA player prop bets. The model scrapes betting lines, calculates expected value (EV), and logs bets that meet the model criteria.

## **Live Site**
💻 [Visit the Live Site](https://d1nzshyp2a8e2d.cloudfront.net/)

## **Tech Stack**
- **Frontend:** React (Vite + TS)  
- **Backend:** AWS Lambda, API Gateway  
- **Infrastructure:** S3 (REST API), CloudFront (CDN), MongoDB Atlas (Data Storage)  

## **How It Works**
1. **Bet Scraping**: The model pings an API every 5 minutes to check for EV betting lines.  
2. **Selection Criteria**: Bets are “placed” if they meet strict expected value and availability conditions.  
3. **Storage & Grading**: The bets are logged and graded at the end of the day.  
4. **Frontend**: Users can select a date and view bets from that day.

**Check out the "About" section of the website for more details.**

## **Installation & Setup**
To run locally:  
```sh
git clone https://github.com/ejjlittle/ev-betting-model.git  
cd ev-betting-model  
npm install  
npm run dev
```

## **Contact**
💼 [LinkedIn](https://www.linkedin.com/in/ethan-little-0587252a2/) | ✉️ [Email](mailto:elittle2@nd.edu)