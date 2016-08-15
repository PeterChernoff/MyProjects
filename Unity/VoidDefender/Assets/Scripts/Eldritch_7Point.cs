using UnityEngine;
using System.Collections;
[RequireComponent(typeof(Attacker))] //protection to ensure that we have an Attacker. Will add Attacker if there isn't one
public class Eldritch_7Point : MonoBehaviour
{

	// Use this for initialization
	private Attacker attacker;
	private Animator anim;
	private bool notTired;
	private Health health;

	void Start()
	{
		notTired = true;
		attacker = gameObject.GetComponent<Attacker>();
		anim = gameObject.GetComponent<Animator>();
		health = gameObject.GetComponent<Health>();
		health.SetSealImmune(true);
	}

	void OnTriggerStay2D(Collider2D col)
	{
		GameObject obj = col.gameObject;
		if (!obj.GetComponent<Defender>())
		{
			//abort if not colliding with Defender
			return;
		}
		else if (obj.GetComponent<Eldritch_Seal>() && health.GetSealImmune())
		{
			//print("Immune: " + health.GetSealImmune());
			//animate when the character can warp
			anim.SetTrigger("warpTrigger");

		}
		else if (transform.position.x < col.transform.position.x)
		{
			return;//Just keep going
		}
		else {
			anim.SetBool("isAttacking", true);
			attacker.Attack(obj);

		}
		//Debug.Log(name + " trigger enter");
	}

}
