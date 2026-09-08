# ManUtd-Performance-Trajectory
# Manchester United Decline — Data Engineering Project

## Problem Statement
Manchester United, undoubtedly the most famous and historic football institution in England who has won 13 Premier League titles, 5 FA Cups, 4 League Cups, 10 Community Shields, 2 Champions League, 1 European Cup Winners' Cup, 1 European Super Cup, 1 Intercontinental Cup, 1 FIFA Club World Cup and a Champions League treble under Sir Alex Ferguson (1986–2013), not only this United side was winning titles but remained a dominant force during Sir Alex's period. After the departure of Sir Alex Ferguson the cub struggled so hard with multiple managers being replaced in short span of time. It also suffered huge losses and made people wonder if that was even reality. From 2013 till this year United haven't won a league title. As a proper United fan, I built this project to understand the "why it hasn't happened yet?" — using historical match results, advanced performance stats, and transfer spend data — to see whether the decline shows up quantifiably (results, squad turnover, underlying performance metrics) or is mostly narrative.

## Goals
- Build an automated, containerized data pipeline (Docker + Airflow +
  Postgres) that extracts, cleans, and models historical and current
  Man United data
- Use this project to deep dive into core data engineering skills — SQL,
  pipeline design, orchestration, and testing 

## Data Sources
- Historical match results: football-data.co.uk
- Advanced team/player stats (2017–present): FBref via `soccerdata`
- Transfer spend & squad value by season: Transfermarkt