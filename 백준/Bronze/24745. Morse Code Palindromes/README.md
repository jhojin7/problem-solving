# [Bronze I] Morse Code Palindromes - 24745 

[문제 링크](https://www.acmicpc.net/problem/24745) 

### 성능 요약

메모리: 108080 KB, 시간: 88 ms

### 분류

구현, 런타임 전의 전처리, 문자열

### 제출 일자

2024년 8월 21일 23:06:27

### 문제 설명

<p>A <strong>palindrome</strong> is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam or racecar or 1881. Phase palindromes ignore capitalization, punctuation, and word boundaries. For example:</p>

<blockquote>
<p>Madam I'm Adam.</p>
</blockquote>

<p>Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes, or dits and dahs. Morse code is named after Samuel Morse, one of the inventors of the telegraph. The international morse code for letters and digits is (Note that the code for upper and lower case letters is the same.):</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/74f37042-07e4-455d-aeb4-f581e05d90df/-/preview/" style="width: 418px; height: 300px;"></p>

<p>A word, number or phrase is a <strong>Morse Code Palindrome</strong> if the morse code for the letters and digits in the word, number or phrase reads the same backwards or forwards (ignoring spaces between character codes. For example:</p>

<p>159</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/a4bdf6de-decd-4d2d-a884-5fb4ab2248df/-/preview/" style="width: 411px; height: 22px;"></p>

<p>Footstool</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6650fad5-1597-40c5-bc3b-c5eaff66e88c/-/preview/" style="width: 718px; height: 22px;"></p>

<p>Write a program which takes as input a string and determines if the string is a Morse Code Palindrome.</p>

### 입력 

 <p>The single input line contains a string of up to 80 characters, possibly including spaces and other non-alphanumeric printable characters.</p>

### 출력 

 <p>The single output line consists of the string YES if the input string (ignoring everything but letters and digits) is a Morse Code Palindrome. Otherwise the output line consists of the string NO. If there are no letters or digits in the input string, the output should be NO.</p>

