package INFLEARN.STEP04

import java.util.*


// https://cote.inflearn.com/contest/10/problem/04-01
// 가장많은 표를 받은 회장 알파벳 출력
/*
in
15
BACBACCACCBDEDE

out
C
*/

private fun solution(n: Int, s: String): Char {
    var answer = ' '
    val map = HashMap<Char, Int>()
    for (x in s.toCharArray()) {
        map[x] = map.getOrDefault(x, 0) + 1
    }
    //System.out.println(map.containsKey('F'));
    //System.out.println(map.size());
    //System.out.println(map.remove('C'));
    var max = Int.MIN_VALUE
    for (key in map.keys) {
        //System.out.println(key+" "+map.get(key));
        if (map[key]!! > max) {
            max = map[key]!!
            answer = key
        }
    }
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    val str = kb.next()
    println(solution(n, str))
}