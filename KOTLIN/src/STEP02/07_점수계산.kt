package STEP02

import java.util.*

// https://cote.inflearn.com/contest/10/problem/02-07
// 연속되서 맞을 경우 점수에 가점이 붙어서 +1 씩 증가함
// 1 1 1 >> 1 2 3 점이 됨
/*
    in
    10
    1 0 1 1 1 0 0 1 1 0

    out
    10
*/
private fun solution(n: Int, arr : IntArray): Int {
    var answer = 0
    var cnt = 0

    for(i in 0 until n){
        // 점수 누적을 위해 cnt 증가 후 더해줌
        if(arr[i] == 1){
            cnt ++
            answer += cnt
        }else{
            cnt = 0
        }
    }

    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    val arr = IntArray(n)

    for(i in 0 until n){
        arr[i] = kb.nextInt()
    }

    println(solution(n, arr))
}