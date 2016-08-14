using UnityEngine;
using System.Collections;


[RequireComponent(typeof(Rigidbody2D))] //protection to ensure that we have a RigidBody2D. Will add RigidBody2D if there isn't one
[RequireComponent(typeof(Health))]
public class Attacker : Creature {

	//[Range(-1f, 1.5f)] public float currentSpeed;//limits the range
	[Tooltip ("Average number of seconds between attackers")]
	public float seenEverySeconds;

	public float attackDamage = 4;

	private float currentSpeed;//limits the range
	private GameObject currentTarget;//what we're attacking
	private Animator anim;
	private Health health;


	private float difficultyAttackAdjustment;

	private bool sealImmune;	
	// Use this for initialization
	void Start() {
		anim = GetComponent<Animator>();
		isAlive = true;

		health = GetComponent<Health>();

		PlayerPrefsSetup();
	}
	void PlayerPrefsSetup()
	{
		//Attack and health is increased or decreased based on difficulty
		float difficulty = PlayerPrefsManager.GetDifficultyLevel();
		health.health = health.health + difficulty - 2;
		difficultyAttackAdjustment = 1f + (difficulty - 2) * .25f;//increase or decrease the damage dealt by 25% increments
		attackDamage = attackDamage * difficultyAttackAdjustment;

		string s = string.Format("Difficulty: {0}. Current health: {1}. Attack strength: {2}. Attack modifier: {3}", difficulty, health.health, attackDamage, difficultyAttackAdjustment);
		//print(s);
	}

	// Update is called once per frame
	void Update() {
		
		transform.Translate(Vector3.left * currentSpeed * Time.deltaTime);//Sends the attacker left
		if (!currentTarget)
		{
			//if the attacker is not in contact with anyone, don't do anything
			anim.SetBool("isAttacking", false);
		}
	}

	public void SetSpeed(float speed)
	{
		//we make this so the attacker can be accessed by the animation
		currentSpeed = speed;
	}
	public void StrikeCurrentTargetBase()
	{
		//deals the creature's base damage
		//if there's a Defender next to me, attack
		if (currentTarget)
		{
			Health health = currentTarget.GetComponent<Health>();
			if (health)
			{
				health.DealDamage(attackDamage);
			}

		}
	}

	public void StrikeCurrentTarget(float damage)
	{
		//This is an alternative method in case I want to adjust the attack in the animator
		if (currentTarget)
		{
			Health health = currentTarget.GetComponent<Health>();
			if (health)
			{
				health.DealDamage(damage);
			}
		}
	}

	public void Attack(GameObject obj)
	{//puts Attacker into attack mode
		currentTarget = obj;
	}
	public void ResetTriggerWarp()//lets us reset a trigger for a character with a warp ability. This is done to avoid continuous triggering
	{
		anim.ResetTrigger("warpTrigger");
	}

}
