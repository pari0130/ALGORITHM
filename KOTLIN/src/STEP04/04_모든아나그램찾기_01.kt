package STEP04

import java.util.*


// https://cote.inflearn.com/contest/10/problem/04-04
// 문자열 중 찾아야 하는 문자열에 해당 하는 값 구하기
// -> 출력설명: {bac}, {acb}, {cba} 3개의 부분문자열이 "abc"문자열과 아나그램입니다.
/*
in
bacaAacba
abc

out
3
*/
private fun solution(a: String, b: String): Int {
    var answer = 0
    val am = HashMap<Char, Int>()
    val bm = HashMap<Char, Int>()
    for (x in b.toCharArray()) bm[x] = bm.getOrDefault(x, 0) + 1
    val L = b.length - 1
    for (i in 0 until L) am[a[i]] = am.getOrDefault(a[i], 0) + 1
    var lt = 0
    for (rt in L until a.length) {
        am[a[rt]] = am.getOrDefault(a[rt], 0) + 1
        if (am == bm) answer++
        am[a[lt]] = am[a[lt]]!! - 1
        if (am[a[lt]] == 0) am.remove(a[lt])
        lt++
    }
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val a = kb.next()
    val b = kb.next()
    print(solution(a, b))
}