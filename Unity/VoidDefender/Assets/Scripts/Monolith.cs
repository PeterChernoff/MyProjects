using UnityEngine;
using System.Collections;

public class Monolith : MonoBehaviour
{

	private Animator animator;
	private int healthVal;
	private bool damaged;
	void Start()
	{
		animator = GetComponent<Animator>();
	}
	void OnTriggerStay2D(Collider2D collider)
	{
		Attacker attacker = collider.gameObject.GetComponent<Attacker>();
		Animator attackAnim = collider.gameObject.GetComponent<Animator>();
		if (!attacker)
		{
			return;
		}
		bool attackerInFront = (attacker.transform.position.x > transform.position.x);//we only want to be attacked if the attacker is in front of it
		//We only want to trigger the animation when the attacker is attacking
		if (attacker && attackAnim.GetBool("isAttacking") && attackerInFront)
		{
			animator.SetTrigger("underAttack");
		}
	}
}
