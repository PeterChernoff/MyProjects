using UnityEngine;
using System.Collections;
[RequireComponent(typeof(Attacker))] //protection to ensure that we have an Attacker. Will add Attacker if there isn't one
public class Eldritch_6Point : MonoBehaviour
{

	// Use this for initialization
	private Attacker attacker;
	private Animator anim;
	private bool notTired;

	void Start()
	{
		notTired = true;
		attacker = gameObject.GetComponent<Attacker>();
		anim = gameObject.GetComponent<Animator>();
	}

	void OnTriggerEnter2D(Collider2D col)
	{
		GameObject obj = col.gameObject;
		if (!obj.GetComponent<Defender>())
		{
			//abort if not colliding with Defender
			return;
		}

		else if (transform.position.x < col.transform.position.x)
		{
			return;//Just keep going
		}
		else if (obj.GetComponent<Monolith>() && notTired)
		{
			anim.SetTrigger("warpTrigger");
			notTired = false;//we only want him to do this once
		}
		else {
			anim.SetBool("isAttacking", true);
			attacker.Attack(obj);

		}
		//Debug.Log(name + " trigger enter");
	}
}
