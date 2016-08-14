using UnityEngine;
using System.Collections;
[RequireComponent(typeof(Attacker))] //protection to ensure that we have an Attacker. Will add Attacker if there isn't one
public class Eldritch_5Point : MonoBehaviour
{

	// Use this for initialization
	private Attacker attacker;
	private Animator anim;

	private int nextUpdate = 1;


	void Start()
	{
		attacker = gameObject.GetComponent<Attacker>();
		anim = gameObject.GetComponent<Animator>();
	}
	void Update()
	{
		if (Time.time >= nextUpdate)
		{
			// Change the next update (current second+1)
			nextUpdate = Mathf.FloorToInt(Time.time) + 1;
			// Call your fonction
			//print("You have selected " + Button.selectedDefender);
		}
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
		else {
			anim.SetBool("isAttacking", true);
			attacker.Attack(obj);

		}
		//Debug.Log(name + " trigger enter");
	}
}
