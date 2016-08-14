using UnityEngine;
using System.Collections;

public class Health : MonoBehaviour {

	public float health = 10f;
	public bool sealImmune;
	
	void Awake()
	{
		sealImmune = false;
	}

	public void DealDamage(float damage)
	{
		health -= damage;
		if (health <= 0)
		{
			//Optionally trigger animation
			DestroyObject();
		}
	}
	public void SetSealImmune(bool immunity)
	{
		sealImmune = immunity;
	}
	public void SetSealImmuneTriggerFalse()
	{
		//for when we want to use the animation triggers
		
		sealImmune = false;
	}

	public bool GetSealImmune()
	{
		return sealImmune;
	}
	public void DestroyObject()
	{

		GetComponent<Collider2D>().enabled = false;//Disables the collider so it doesn't trigger anything else
		Creature creature = GetComponent<Creature>();
		
		GetComponent<Animator>().SetTrigger("isDead");
		creature.SetLife(false);
		
		
		Destroy(gameObject, 1f);
		
	}
}
