package STEP03

import java.util.*

// https://cote.inflearn.com/contest/10/problem/03-05
// 연속된 자연수의 합으로 입력값 n이 되는 경우를 출력
/*
in
15

out
3
*/

private fun solution(n: Int): Int {
    var answer = 0
    var sum = 0
    val m = n / 2 + 1 // 절반 이상의 수 이후 부터는 연속된 수를 더하면 값을 넘기 때문에 n/2+1 까지.. ex) 8일때 4+5는 넘어감.
    val arr = IntArray(m)
    for (i in 0 until m) arr[i] = i + 1
    var lt = 0
    for (rt in 0 until m) {
        sum += arr[rt]
        if (sum == n) answer++
        while (sum >= n) {
            sum -= arr[lt++]
            if (sum == n) answer++
        }
    }
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    System.out.print(solution(n))
}