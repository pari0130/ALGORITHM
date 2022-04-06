package INFLEARN.STEP04

import java.util.*


// https://cote.inflearn.com/contest/10/problem/04-02
// 두 단어의 구성이 같으면 yes (a 가 2개 b가 2개 등등..)
/*
in
AbaAeCe
baeeACA

out
YES
*/

private fun solution(s1: String, s2: String): String? {
    val answer = "YES"
    val map = HashMap<Char, Int?>()
    for (x in s1.toCharArray()) {
        map[x] = map.getOrDefault(x, 0)!! + 1
    }
    for (x in s2.toCharArray()) {
        if (!map.containsKey(x) || map[x] == 0) return "NO"
        map[x] = map[x]!! - 1
    }
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val a = kb.next()
    val b = kb.next()
    print(solution(a, b))
}