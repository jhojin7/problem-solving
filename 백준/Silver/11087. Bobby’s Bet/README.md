# [Silver II] Bobby’s Bet - 11087 

[문제 링크](https://www.acmicpc.net/problem/11087) 

### 성능 요약

메모리: 112792 KB, 시간: 496 ms

### 분류

다이나믹 프로그래밍, 수학, 확률론

### 제출 일자

2024년 8월 20일 15:37:15

### 문제 설명

<p>Bobby and Betty have a bet. Betty bets Bobby that he cannot roll an S-sided die (having values 1 through S) and obtain a value ≥ R on at least X out of Y rolls. Betty has a variety of dice with different numbers of sides S, and all her dice are fair (for a given die, each side’s outcome is equally likely). In order to observe statistically rare events while still giving Bobby a reason to bet, Betty offers Bobby W to 1 odds on each encounter. For example, suppose Betty bets Bobby 1 bitcoin that he can’t roll at least a 5 on a 6-sided die at least two out of three times; if Bobby does, she would give him 3 times his initial bet (i.e. she would give him 3 bitcoins). Should Bobby take the bet (is his expected return greater than his original bet)?</p>

### 입력 

 <p>Input begins with an integer 1 ≤ N ≤ 10 000, representing the number of cases that follow. The next N lines each contain five integers, R, S, X, Y , and W. Their limits are 1 ≤ R ≤ S ≤ 20, 1 ≤ X ≤ Y ≤ 10, and 1 ≤ W ≤ 100.</p>

### 출력 

 <p>For each case, output “yes” if Bobby’s expected return is greater than his bet, or “no” otherwise. Bobby is somewhat risk averse and does not bet if his expected return is equal to his bet.</p>

